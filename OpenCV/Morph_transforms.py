import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.jpg', cv2.IMREAD_GRAYSCALE)
_,mask = cv2.threshold(img,150,255,cv2.THRESH_BINARY_INV)

kernal = np.ones((5,5), np.uint8)

dilation = cv2.dilate(mask,kernal)
erosion = cv2.erode(mask,kernal,iterations=2)
opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal) # erosion -> dilation
closing = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal) # dilation -> erosion
mg = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal) # dilation - erosion
th = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal) # image - opening_of_image

titles = ['image','mask','dilation','erosion','opening','closing','mg','th']
images = [img,mask,dilation,erosion,opening,closing,mg,th]

for i in range(8):
    plt.subplot(2, 4, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

# Morphological transformation is an image transformation based on image shape.
# Normally performed on binary images(diff from grayscale!).
# EROSION : A pixel in the original image (either 255 or 0) will be considered 255 only if all the pixels under the kernel is 255, 
# 			otherwise it is eroded (made to zero).
#			WHITE REGION DECREASES
# DILATION(opp. of erosion) : A pixel element in the original image is 255 if atleast one pixel under the kernel is 255.
#			  				  WHITE REGION INCREASES
