import cv2
import numpy as np

def empty(x):
    pass # does nothing

cap = cv2.VideoCapture(0)

cv2.namedWindow('Tracker')
cv2.createTrackbar('LH', 'Tracker', 0, 255, empty)
cv2.createTrackbar('LS', 'Tracker', 0, 255, empty)
cv2.createTrackbar('LV', 'Tracker', 0, 255, empty)
cv2.createTrackbar('UH', 'Tracker', 0, 255, empty)
cv2.createTrackbar('US', 'Tracker', 0, 255, empty)
cv2.createTrackbar('UV', 'Tracker', 0, 255, empty)

while 1:
    #frame = cv2.imread('Smarties.jpg',1)
    (ret, frame) = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #BGR to HSV colourspace conversion

    l_h = cv2.getTrackbarPos('LH', 'Tracker')
    l_s = cv2.getTrackbarPos('LS', 'Tracker')
    l_v = cv2.getTrackbarPos('LV', 'Tracker')

    u_h = cv2.getTrackbarPos('UH', 'Tracker')
    u_s = cv2.getTrackbarPos('US', 'Tracker')
    u_v = cv2.getTrackbarPos('UV', 'Tracker')

    
    l = np.array([l_h,l_s,l_v])
    u = np.array([u_h,u_s,u_v])

    mask = cv2.inRange(hsv, l, u) # Returns 2D matrix containing 255 if h AND s AND v values are
                                  # in between the upper and lower bound specified values otherwise contains 0

    b,g,r = cv2.split(frame)
    b=((np.multiply(b.astype(np.int32),mask.astype(np.int32)))/255).astype(np.uint8) # np.multiply performs element-wise array multiplication
    g=((np.multiply(g.astype(np.int32),mask.astype(np.int32)))/255).astype(np.uint8) # [array}.astype({datatype}) converts array datatype 
    r=((np.multiply(r.astype(np.int32),mask.astype(np.int32)))/255).astype(np.uint8)
    detected = cv2.merge((b,g,r))
    
    cv2.imshow('object', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('detected',detected)


    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
