import cv2
import numpy as np

img = cv2.resize(cv2.imread('me.jpg',1),(660,512))
filimg = cv2.resize(cv2.imread('me.jpg',1),(660,512))
medBlur=cv2.medianBlur(img,5)

kernel=np.ones((3,3),int)
kernel=(-1)*kernel
kernel[1,1]=8

cv2.filter2D(img,-1,kernel,filimg)
cv2.filter2D(medBlur,-1,kernel,medBlur)
cv2.imshow('Blur&filtered',medBlur)
cv2.imshow('filtered',filimg)
cv2.imshow('unfiltered',img)

print(kernel)

cv2.waitKey(0)
cv2.destroyAllWindows()