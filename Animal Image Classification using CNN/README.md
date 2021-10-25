# Animal classification using CNN

## Goals
The goal from this project is to classify species of animal based on images, so it can automatically help identify animals in the wild.

## Data Understanding
The dataset is from [Animals10](https://www.kaggle.com/alessiocorrado99/animals10) dataset in Kaggle. The dataset have `10` class clasification and `26.2k` total images. But for this classification we only choose 3 class, that is `horse`, `chicken`, and `spider`. The distribution of image for each class, you can see in below :

![image](https://user-images.githubusercontent.com/61934759/138651973-b7c08dd8-0f9e-4bed-afe5-120d1d59f235.png)


## Data Preparation
In this step, the data will be process before going to modelling.
* Rename dataset class from `italian` to `english`. 
* Select class `horse`, `chicken`, and `spider`, so the total image in dataset is `10542`.
* Split the dataset into `80%` data train and `20%` data validation. 
* Augmentation the data using methods _ImageDataGenerator_ from tensorflow library.

## Modelling
Train data of animal from 3 different species using Convolutional Neural Network (CNN). From the train using `10` epoch, the model have accuracy `92%` for train accuracy and `93%` for validation accuracy.

![train history](https://user-images.githubusercontent.com/61934759/138654166-9ff109ed-ba77-4163-98fa-3f7ebd568a05.png)