# Vehicle Detection
[![Udacity - Self-Driving Car NanoDegree](https://s3.amazonaws.com/udacity-sdc/github/shield-carnd.svg)](http://www.udacity.com/drive)


In this project, your goal is to write a software pipeline to detect vehicles in a video (start with the test_video.mp4 and later implement on full project_video.mp4), but the main output or product we want you to create is a detailed writeup of the project.  Check out the [writeup template](https://github.com/udacity/CarND-Vehicle-Detection/blob/master/writeup_template.md) for this project and use it as a starting point for creating your own writeup.  

The Project
---

The goals / steps of this project are the following:

* Perform a Histogram of Oriented Gradients (HOG) feature extraction on a labeled training set of images and train a classifier Linear SVM classifier
* Optionally, you can also apply a color transform and append binned color features, as well as histograms of color, to your HOG feature vector. 
* Note: for those first two steps don't forget to normalize your features and randomize a selection for training and testing.
* Implement a sliding-window technique and use your trained classifier to search for vehicles in images.
* Run your pipeline on a video stream (start with the test_video.mp4 and later implement on full project_video.mp4) and create a heat map of recurring detections frame by frame to reject outliers and follow detected vehicles.
* Estimate a bounding box for vehicles detected.

Here are links to the labeled data for [vehicle](https://s3.amazonaws.com/udacity-sdc/Vehicle_Tracking/vehicles.zip) and [non-vehicle](https://s3.amazonaws.com/udacity-sdc/Vehicle_Tracking/non-vehicles.zip) examples to train your classifier.  These example images come from a combination of the [GTI vehicle image database](http://www.gti.ssr.upm.es/data/Vehicle_database.html), the [KITTI vision benchmark suite](http://www.cvlibs.net/datasets/kitti/), and examples extracted from the project video itself.   You are welcome and encouraged to take advantage of the recently released [Udacity labeled dataset](https://github.com/udacity/self-driving-car/tree/master/annotations) to augment your training data.  

Some example images for testing your pipeline on single frames are located in the `test_images` folder.  To help the reviewer examine your work, please save examples of the output from each stage of your pipeline in the folder called `ouput_images`, and include them in your writeup for the project by describing what each image shows.    The video called `project_video.mp4` is the video your pipeline should work well on.  

[image1]: ./sample_dataset.png
[image2]: ./sample_hog.png
[image3]: ./sample_heat.png
[image4]: ./sample_heat_.png
[image5]: ./sample_heat2.png

Histogram of Oriented Gradients (HOG)
---

I started by reading in all the vehicle and non-vehicle images. Here is an example of one of each of the vehicle and non-vehicle classes:
![alt text][image1]


In requirement of building a classifier that can regconize if a car exists in a given image or not, I use HOG feature, which is good enough for image classification. And the model I chose to train is Multilayer Perceptron Classifier, which is supported by sklearn library.

This model gives an impressive result with 99% accuracy on test set. The color space I chose is one of this three: YUV, Lab or YCrCb, because it gives me the best result on test image without any wrong detection.

![alt text][image2]


Sliding Window Search apply on test image and corresponding heatmaps
---
Restricted area of sliding window is from 400px to 680px in width and increase the window size +20 pixel each time, if window size too small can increase the number of image must to be detected. In case there is a wrong detection, the heat image will looks like below:
![alt text][image3]

Therefore, in each time we draw a detected window on mask image, we just "add heat" (+=1) for all pixels within windows where a positive detection is reported. That's how we made a heat image.

Upgrade the main function with thresholds, and re-draw the mask image based on heat map we just created.
![alt text][image4]

The result when we apply on test image:
![alt text][image5]

Video result and improvement
---
I experiment with thresholds value equals 3, and 4. I just considering another way to improve step remove wrong car detection, that's the reason why I lost detection in 1-2s in this video. There are two solution I'm thinking about:

* Try to use another classifier algorithm like SVM (as suggestion in class)
* Get more data for training set
* Use other way to remove wrong detection, like calculate distance of middle of rectangle windows in each frames, but when I tried to apply it, it takes more time to process frame.

Any help and suggestion would be greatly appreciated!


