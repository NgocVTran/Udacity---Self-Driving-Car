# **Finding Lane Lines on the Road** 

## Writeup Template
The first project of Udacity - Self-Driving Car Nano Degree.
---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:
* Make a pipeline that finds lane lines on the road
* Reflect on your work in a written report


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Reflection

### 1. Describe the pipeline

My pipeline consisted of the following steps:
1. Define color section criteria
2. Apply Canny Edfe Detection
3. Define restricted area
4. Apply Hough Transform on this area
5. Draw lines from detected line segments
6. Apply to video

[result]: ./lane_detected_images/solidWhiteCurve.jpg "Test white lane"

I don't use the default template and the way I draw lines is picking up randomly a detected line segments and scale it. How was I calculate the line function and start-, end-point of line was decribed in jupyter notebook file.


### 2. Identify potential shortcomings with current pipeline

As some suggestions of my mentor, increasing threshold of color can get rid of spurious lines. It's possible to increase it from 215 to 220, I will receive the thinner lines, which gives smaller number of line segments in the next step.

Desreasing kernel-size of Gaussian Filter will remove the noise, too. All the other parameters like rho, theta could be tried to modify to get the best value.



### 3. Suggest possible improvements to your pipeline

A possible improvement would be to calculate the average coordinate of line segments to find out a better result, instead of taking line segment randomly.

Another potential improvement could be to try to find another algorithm, even using Deep Learning - like using CNN and Deconvolution Neural Network to find the road segmentation of images.
