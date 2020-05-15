import cv2
import numpy as np

img = cv2.resize(cv2.imread('me.jpg',1),(660,512))
fadimg = cv2.resize(cv2.imread('me.jpg',1),(660,512))
embimg = cv2.resize(cv2.imread('me.jpg',1),(660,512))

fade_kernel=np.array([[0.04,0.04,0.04,0.04,0.04],
				[0.04,0.04,0.04,0.04,0.04],
				[0.04,0.04,0.04,0.04,0.04],
				[0.04,0.04,0.04,0.04,0.04],
				[0.04,0.04,0.04,0.04,0.04]])

emboss_kernel=np.array([[-2,-1,0],
						[-1,1,1],
						[0,1,2],])

cv2.filter2D(img,-1,fade_kernel,fadimg)
cv2.filter2D(img,-1,emboss_kernel,embimg)
cv2.imshow('faded',fadimg)
cv2.imshow('embossed',embimg)
cv2.imshow('me',img)

cv2.waitKey(0)
cv2.destroyAllWindows()