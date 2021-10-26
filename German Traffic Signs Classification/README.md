# German Traffic Signs Classification
Some implementation computer vision that is important for self-driving cars is detection, classification, and segmentation of various types of object. In this project we will make machine learning model about implementation computer vision to self-driving cars.

## Data Understanding
The dataset is from [German Traffic Sign Kaggle](https://www.kaggle.com/saadhaxxan/germantrafficsigns). The dataset have:
* 43 class with different traffic signs type
* More than 50.000 image in dataset
* The data was take from real traffic signs

In the signnames.csv, the file containing id and class name. From using method head() from pandas, there is :

![class name](https://user-images.githubusercontent.com/61934759/138904762-7428f37c-57fe-4cd1-8fa2-f1a5aabaa227.png)

## Data Preparation
In this step, the data will be process before going to modelling.
* Define features and labels for training data
* Define features and labels for testing data
* Split training data into train and val

Result of visulization of distribution class in train data, val data and test data.
![distribution](https://user-images.githubusercontent.com/61934759/138905925-ee15fab2-b251-4754-ad89-d27511984763.png)

# Modelling
Train data of animal from 3 different species using Convolutional Neural Network (CNN). From the train using `25` epoch, the model have accuracy `95%` for train accuracy,  `98%` for validation accuracy, `95%` for testing accuracy.

![accuracy history](https://user-images.githubusercontent.com/61934759/138906548-8074be2f-e275-448d-b876-408bbf68fed2.png)

