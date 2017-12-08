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

[image5]: ./output_images/birdview.png
[image5]: ./output_images/birdview.png
[image5]: ./output_images/birdview.png


Camera Calibration
---
Calculate Camera Calibration using chessboard images and test with some image:

* Before:
<img scr="camera_cal/calibration1.jpg" width="500px">
![alt text][image1]
* After:
![alt text][image2]

Pipeline (test images)
---
* Provide an example of a distortion-corrected image
![alt text][image3]

* Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image. Provide an example of a binary image result.

In 'thresholded_binary(undistorted_img)' function, convert the image to HLS color-space, then use the OpenCV Sobel function to get where the gradient of an image in the X direction. Then convert the image the HSV color-space with S-channel threshold
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








