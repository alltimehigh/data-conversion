import os
import cv2

"""
Automatic image channel conversion
Image three-channel to four-channel
"""

colpath = []
path = './images'

for root, dirs, files in os.walk(path):
    print("ROOT : ", root)
    print("DIRS : ",dirs)
    print("FILES : ", files)

for root, dirs, files in os.walk(path):
    for img in files:
        if img.endswith((".png", ".jpg", ".jpeg", ".bmp")):
            # print("FILE NAME : ", img)
            colpath.append(root + "/" + img)

print("ALL PATH : ", colpath)

from PIL import Image

for c in colpath:
    img = Image.open(c)
    # Directly output the number of channels of the image
    print("INFO. IMG.: ", img,"; Channels : ", len(img.split()), "; Details : ", img.split())
    key = len(img.split())
    if key == 3:
        cvimg = cv2.imread(c)
        img_with_alpha = cv2.cvtColor(cvimg, cv2.COLOR_RGB2RGBA)
        img_with_alpha[:,:, 3] = 255

        cv2.imwrite(c,img_with_alpha)


