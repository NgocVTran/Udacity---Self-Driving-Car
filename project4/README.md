## Advanced Lane Finding
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)


In this project, your goal is to write a software pipeline to identify the lane boundaries in a video, but the main output or product we want you to create is a detailed writeup of the project.  Check out the [writeup template](https://github.com/udacity/CarND-Advanced-Lane-Lines/blob/master/writeup_template.md) for this project and use it as a starting point for creating your own writeup.  

Advanced Lane Finding Project
---
The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[image1]: ./camera_cal/calibration1.jpg "Before"
[image2]: ./output_images/camera_cal_outp/0.jpg "After"
[image3]: ./output_images/before_after.png
[image4]: ./output_images/threshold.png
[image5]: ./output_images/birdview.png
[image6]: ./output_images/grayscale.png
[image7]: ./output_images/histogram.png
[image8]: ./output_images/slide_window.png
[image9]: ./output_images/slide_window2.png
[image10]: ./output_images/lane_detection.png
[image11]: ./output_images/test_images_outp/test5.jpg
[image12]: ./sample1.png
[image13]: ./sample2.png

Change after last review:
---
* Some text correction: I keep using the HLS color space with S-channel and corrected my writeup text :) thx
* You're right about my math form to calculate lane deviation. Actually I got the same form as your suggestion but wrong typing code :P
First we need to calculate the center, which is alread 'div 2'. Then compute the distance between it and center of the image.
* Correction of my bug: mixed height and width of image.
* Try another color space:
I have tried L-channel of LUV color space as your suggestion with some different thresholds, but the result when I apply it on test images was not good, although it generates a cleaner binary image.

![alt text][image12]

![alt text][image13]

So I guess, I need to keep trying another color space, or find the way to combine them together to improve the algorithm.

Camera Calibration
---
Calculate Camera Calibration using chessboard images and test with some image:

* Before:
![alt text][image1]
* After:
![alt text][image2]

Pipeline (test images)
---
* Provide an example of a distortion-corrected image
![alt text][image3]

* Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image. Provide an example of a binary image result.

In 'thresholded_binary(undistorted_img)' function, convert the image to HLS color-space, then use the OpenCV Sobel function to get where the gradient of an image in the X direction. Then convert the image the HLS color-space with S-channel threshold.
![alt text][image4]

* Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

The first step is calculate the source and destination points. I chose the hardcode the source and destination points in the following manner:

| Source      |    Destination	   |
|:------------|:-------------------|
| 585, 460    | 320, 0			   |
| 203, 720    | 320, 720           |
| 1127, 720	  |	960, 720    	   |
| 695, 460	  | 960, 0             |

Perspective transform was working as expected by drawing the src and dst points onto a test image and its warped counterpart to verify that the lines appear parallel in the warped image (by using function cv2.getPerspectiveTransform(src, dst))
![alt text][image5]

* Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?
Get the grayscale image of bird view, then take the histogram of this image. Find the peak of the left and right halves of the histogram, these will be the starting point for the left and right lines.
![alt text][image6]


Histogram:

![alt text][image7]


With this histogram I am adding up the pixel values along each column in the image. Use a sliding window and fit a polynomial to those pixel positions, by placed around the line centers, to find and follow the lines up to the top of the frame.
![alt text][image8]

![alt text][image9]


Draw the found lane lines onto a binary warped image, then unwarp and overlay on the original image.

![alt text][image10]

* Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

Calculate the radius of curvature based on pixel values (function 'get_curvature()'), _but our images are in pixel space and need to be converted into meters. 

Asume that the camera is in the middle of car, then I calculate center of left and right lane. Lane deviation is calculated by half of subtraction of center lane minus center of image's width.

* Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

![alt text][image11]

All the images result are on this folder:
'output_images/test_images_outp'

It was also shown on jupyter notebook file code, too.


Pipeline (video)
---
Same as project 1, I applied this algorithm for all frames of the video. Video result can be found on folder:
'output_images/project_video.mp4'


Discussion
---
There are still much things to do to improve the result of challenge video:
'output_images/challenge_video.mp4'

This algorithm detect the wrong left lane when there is a shadow on the road, or when the car runs on sunny. I was experimented by trying another threshold, color space but I still can't reach the solution. Any advance is greatly appreciated, then I should improve this algorithm in future.