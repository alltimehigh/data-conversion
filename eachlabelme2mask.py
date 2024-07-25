import os
import json
import numpy as np
import cv2

# read json file
with open("./test/cow.json", "r") as f:
    data = f.read()
# convert str to json objs
data = json.loads(data)
 
# get the points 
points = data["shapes"][0]["points"]
points = np.array(points, dtype=np.int32)   # tips: points location must be int32
print(points )
# read image to get shape
image = cv2.imread("./test/cow.jpg")

# create a blank image
mask = np.zeros_like(image, dtype=np.uint8)
 
# fill the contour with 255
cv2.fillPoly(mask, [points], (255, 255, 255))
 
# save the mask 
cv2.imwrite("mask.png", mask)

