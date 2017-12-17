# Behaviorial Cloning Project

[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)

Overview
---
This repository contains starting files for the Behavioral Cloning Project.

In this project, you will use what you've learned about deep neural networks and convolutional neural networks to clone driving behavior. You will train, validate and test a model using Keras. The model will output a steering angle to an autonomous vehicle.

We have provided a simulator where you can steer a car around a track for data collection. You'll use image data and steering angles to train a neural network and then use this model to drive the car autonomously around the track.


The Project
---
The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report

### Dependencies
This lab requires:

* [CarND Term1 Starter Kit](https://github.com/udacity/CarND-Term1-Starter-Kit)

The lab enviroment can be created with CarND Term1 Starter Kit. Click [here](https://github.com/udacity/CarND-Term1-Starter-Kit/blob/master/README.md) for the details.

The following resources can be found in this github repository:
* drive.py
* video.py
* README.md
* Behavioral-Cloning.ipynb
* model_10_epochs.h5

The simulator can be downloaded from the classroom. In the classroom, we have also provided sample data that you can optionally use to help train your model.


<a href="https://www.youtube.com/watch?v=QJ3R5j6arOY&feature=youtu.be" target="_blank"><img src="http://img.youtube.com/vi/YOUTUBE_VIDEO_ID_HERE/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>


Files Submitted & Code Quality
---

* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network
* writeup_report.md or writeup_report.pdf summarizing the results

[image1]: ./model.png



I use the model that published by autonomous vehicle team at NVIDIA. Here is paper link: 
<a href="https://arxiv.org/pdf/1604.07316.pdf">NVIDIA Model</a>

I have tried to rebuild LeNet model, and some more suggestion from the course. But finally I picked NVIDIA Model. 

#### Structure 10 epochs model without dropout:
Layer (type)                 Output Shape              Param #   
_________________________________________________________________
lambda_1 (Lambda)            (None, 160, 320, 3)       0         
_________________________________________________________________
cropping2d_1 (Cropping2D)    (None, 65, 320, 3)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 31, 158, 24)       1824      
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 14, 77, 36)        21636     
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 5, 37, 48)         43248     
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 3, 35, 64)         27712     
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 1, 33, 64)         36928     
_________________________________________________________________
flatten_1 (Flatten)          (None, 2112)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 1164)              2459532   
_________________________________________________________________
dense_2 (Dense)              (None, 100)               116500    
_________________________________________________________________
dense_3 (Dense)              (None, 50)                5050      
_________________________________________________________________
dense_4 (Dense)              (None, 1)                 51        
_________________________________________________________________


#### Training process for 10 epochs model:
Train on 38572 samples, validate on 9644 samples 
Epoch 1/10 
38572/38572 [==============================] - 643s 17ms/step - loss: 0.0119 - val_loss: 0.0109 
Epoch 2/10 
38572/38572 [==============================] - 599s 16ms/step - loss: 0.0099 - val_loss: 0.0110 
Epoch 3/10 
38572/38572 [==============================] - 598s 16ms/step - loss: 0.0097 - val_loss: 0.0105 
Epoch 4/10 
38572/38572 [==============================] - 599s 16ms/step - loss: 0.0096 - val_loss: 0.0108 
Epoch 5/10 
38572/38572 [==============================] - 599s 16ms/step - loss: 0.0095 - val_loss: 0.0104 
Epoch 6/10 
38572/38572 [==============================] - 597s 15ms/step - loss: 0.0094 - val_loss: 0.0117 
Epoch 7/10 
38572/38572 [==============================] - 598s 16ms/step - loss: 0.0093 - val_loss: 0.0106 
Epoch 8/10 
38572/38572 [==============================] - 599s 16ms/step - loss: 0.0091 - val_loss: 0.0107 
Epoch 9/10 
38572/38572 [==============================] - 603s 16ms/step - loss: 0.0091 - val_loss: 0.0105 
Epoch 10/10 
38572/38572 [==============================] - 630s 16ms/step - loss: 0.0087 - val_loss: 0.0110




This model was implemented by keras, with MSE as loss function and Adam algorithm as optimizer.

Model Structure:


![alt text][image1]

All code was written in file 'model.py'. My jupyter notebook 'Behavioral-Cloning.ipynb' describes how this code running step by step.

Model Architecture and Training Strategy
---
The data is normalized in the model using a Keras lambda layer. Preprocessig data included three step (using with multiple cameras):
* Data augmentation: flipping the images and steering measurements
* Normalizing data and mean-centering data
* Cropping images in Keras

## Improvement
* The model_4p_dropout.h5 was trainned 4 epochs with dropout .50. The autonomous car keep staying on the left side and goes out of the road. So when I add dropout and increase number of epoch to 7, this model still have overfitting.

* Then I decided to remove dropout and increase epoch to 10, that's my last model. Although it stays in the middle of road, but sometimes fail in the corner that it must turns right. Because the training data of turning right is too little. 

Maybe I should collect more data by training the car goes counter-clockwise? Or start using flipping images? Or try another Model like VGG-16. There are still so many things I could do to improve my model.

Any help will be appreciated!

