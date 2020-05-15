import cv2
import numpy as np
import winsound

img = cv2.resize(cv2.imread('me.jpg',1),(640,480))

#LEFT DRUM
cv2.rectangle(img,(100,430),(240,390),(0,0,0),-1)
cv2.rectangle(img,(90,420),(250,400),(42,42,165),-1)

#RIGHT DRUM
cv2.rectangle(img,(420,430),(560,390),(0,0,0),-1)
cv2.rectangle(img,(410,420),(570,400),(42,42,165),-1)

cv2.imshow('sample',img)


cv2.waitKey(0)
cv2.destroyAllWindows()




# def empty(x):
# 	pass

# cv2.namedWindow('Tracker')
# cv2.createTrackbar('LH', 'Tracker', 0, 255, empty)
# cv2.createTrackbar('LS', 'Tracker', 0, 255, empty)
# cv2.createTrackbar('LV', 'Tracker', 0, 255, empty)
# cv2.createTrackbar('UH', 'Tracker', 0, 255, empty)
# cv2.createTrackbar('US', 'Tracker', 0, 255, empty)
# cv2.createTrackbar('UV', 'Tracker', 0, 255, empty)

# cap = cv2.VideoCapture(0)
# print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) #480
# print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #640

# while 1 :
# 	_,frame = cap.read()
# 	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# 	l_h = cv2.getTrackbarPos('LH', 'Tracker')
# 	l_s = cv2.getTrackbarPos('LS', 'Tracker')
# 	l_v = cv2.getTrackbarPos('LV', 'Tracker')
# 	u_h = cv2.getTrackbarPos('UH', 'Tracker')
# 	u_s = cv2.getTrackbarPos('US', 'Tracker')
# 	u_v = cv2.getTrackbarPos('UV', 'Tracker')

# 	l = np.array([l_h,l_s,l_v])
# 	u = np.array([u_h,u_s,u_v])
	
# 	mask = cv2.inRange(hsv, l, u)
# 	flip_mask = np.flip(mask,1)

# 	#LEFT DRUM
# 	cv2.rectangle(frame,(100,410),(240,370),(42,42,165),-1)
# 	cv2.rectangle(frame,(90,400),(250,380),(0,0,0),-1)

# 	#RIGHT DRUM
# 	cv2.rectangle(frame,(420,410),(560,370),(42,42,165),-1)
# 	cv2.rectangle(frame,(410,400),(570,380),(0,0,0),-1)


# 	flip_frame = np.flip(frame,1) #'1' > vertical axis; flips the image matrix about this axis

# 	cv2.imshow('Aerodrums',flip_frame)
# 	cv2.imshow('mask',flip_mask)

# 	if cv2.waitKey(1) == ord('q'):
# 		break

# cap.release()
# cv2.destroyAllWindows()
