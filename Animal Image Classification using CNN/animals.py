# -*- coding: utf-8 -*-
"""Animals

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wRSJTrDIi8QYkaz-jf13LuBIFmxjFwAY

# Animals Classification
Yoga Mileniandi

### Load the library
"""

import os
import shutil
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense, Flatten, Dropout, BatchNormalization, Conv2D, MaxPooling2D
from tensorflow.keras.models import Sequential
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import ImageDataGenerator, img_to_array, load_img
from zipfile import ZipFile
from PIL import Image

"""### Get data From Kaggle"""

# Set Kaggle API Permission
! pip install -q kaggle
from google.colab import files
files.upload()
! mkdir ~/.kaggle
! cp kaggle.json ~/.kaggle/
! chmod 600 ~/.kaggle/kaggle.json

# Get Dataset From Kaggle
!kaggle datasets download -d alessiocorrado99/animals10

path = 'animals10.zip'
with ZipFile(path, 'r') as zip_ref:
    zip_ref.extractall('working')

path = 'working/raw-img'
os.listdir(path)

"""### Preprocessing"""

# Rename directories
categories = {'cane': 'dog', "cavallo": "horse", "elefante": "elephant", 
              "farfalla": "butterfly", "gallina": "chicken", "gatto": "cat",
              "mucca": "cow", "pecora": "sheep", "scoiattolo": "squirrel","ragno":"spider"}
for origin,translate in categories.items():
  os.rename(os.path.join(path, origin), os.path.join(path, translate))

# Check
for animal in os.listdir(path):
  print(f"{animal} : {len(os.listdir(os.path.join(path, animal)))}")

# Create Train and Validation Directory
TRAIN_DIR = 'working/train'
VAL_DIR = 'working/val'

os.mkdir(TRAIN_DIR)
os.mkdir(VAL_DIR)

# create directory 
dir_name = ['horse', 'chicken', 'spider']
for dir in dir_name:
  os.mkdir(os.path.join(TRAIN_DIR, dir))
  os.mkdir(os.path.join(VAL_DIR, dir))

# Select horse, chicken and spider
# So the total dataset is 10542
for dir in dir_name:
  dir_file = os.path.join(path, dir)
  train = os.path.join(TRAIN_DIR, dir)
  val = os.path.join(VAL_DIR, dir)

  train_split, val_split = train_test_split(os.listdir(dir_file), test_size = 0.2)
  for filename in train_split:
    shutil.copy(os.path.join(dir_file, filename), os.path.join(train, filename))
  for filename in val_split:
    shutil.copy(os.path.join(dir_file, filename), os.path.join(val, filename))

for dir in dir_name:
  for i in [TRAIN_DIR, VAL_DIR]:
    current_dir = os.path.join(i, dir)
    print(current_dir)
    print(f"Number of Files : {len([file for file in os.listdir(current_dir)])}")

train_datagen = ImageDataGenerator(
    rescale = 1./255,
    rotation_range = 20,
    horizontal_flip = True,
    shear_range = 0.2,
    fill_mode = 'nearest'
)

val_datagen = ImageDataGenerator(
    rescale = 1./255
)

IMG_HEIGHT = 128
IMG_WIDTH = 128
train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size = (IMG_HEIGHT,IMG_WIDTH),
    batch_size = 32,
    class_mode = 'categorical'
)

val_generator = train_datagen.flow_from_directory(
    VAL_DIR,
    target_size = (IMG_HEIGHT,IMG_WIDTH),
    batch_size = 32,
    class_mode = 'categorical'
)

"""### Modelling"""

model = Sequential()

model.add(Conv2D(64,(3,3), activation = 'relu', input_shape = (IMG_HEIGHT,IMG_WIDTH,3)))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Conv2D(64,(3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Conv2D(128,(3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Conv2D(128,(3,3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))

model.add(Dense(3, activation='softmax'))

model.compile(optimizer="adam",
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

class CallBack(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('val_accuracy') > 0.92 and logs.get('accuracy') > 0.92:
            self.model.stop_training = True
            print('Akurasi telah mencapai 92%')
            
callback = CallBack()

hist =model.fit(
        train_generator,
        steps_per_epoch=8432/32,  
        epochs=77, 
        validation_data=val_generator, 
        validation_steps=2110/32,  
        verbose=1,
        callbacks = [callback])

plt.plot(hist.history['accuracy'])
plt.plot(hist.history['val_accuracy'])
plt.title('Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Test'])

plt.plot(hist.history['loss'])
plt.plot(hist.history['val_loss'])
plt.title('Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Test'])

"""### Save to TFLite format"""

# Konversi model.
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with tf.io.gfile.GFile('model.tflite', 'wb') as f:
  f.write(tflite_model)

