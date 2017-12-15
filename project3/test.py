import csv
import cv2
import numpy as np

lines = []
with open("./setup/data/driving_log.csv") as csvfile:
    reader = csv.reader(csvfile) 
    for line in reader: 
        lines.append(line)

images = []
measurements = []
for line in lines:
    source_path = line[0]
    filename = source_path.split("/")[-1]
    current_path = "./setup/data/IMG/" + filename
    image = cv2.imread(current_path)
    images.append(image)
    measurement = float(line[3])
    measurements.append(measurement)

X_train = np.array(images)
y_train = np.array(measurements)	