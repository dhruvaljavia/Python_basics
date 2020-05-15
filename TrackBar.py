import cv2
import numpy as np

def empty(x):
    x=x
    
img = np.zeros((400,400,3),np.uint8)
cv2.namedWindow('color') # Creates a named window with 'color' as title

cv2.createTrackbar('B','color', 0, 255, empty)  # 'B' > track bar name
												# 'color' > window name
												# '0' > min value
												# '255' > max value
												# 'empty' > called when trackbar value changes
cv2.createTrackbar('G', 'color', 0, 255, empty)
cv2.createTrackbar('R', 'color', 0, 255, empty)

while(1):
    cv2.imshow('color', img)
    if cv2.waitKey(1) == 27:
        break

    b = cv2.getTrackbarPos('B', 'color')
    g = cv2.getTrackbarPos('G', 'color')
    r = cv2.getTrackbarPos('R', 'color')

    img[:] = [b, g, r] # Sets row values to [b,g,r]

cv2.destroyAllWindows()
