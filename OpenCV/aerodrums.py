import cv2
import numpy as np
import winsound
# CAP_PROP_FRAME_HEIGHT = 480
# CAP_PROP_FRAME_WIDTH = 640

#Create cap object
cap = cv2.VideoCapture(0)

#Define kernel for dilation of drum stick tip
kernel = np.ones((7,7),np.uint8)

#HSV ranges for detecting drum stick tip
l = np.array([0,237,132])
u = np.array([21,255,255])

#Control for beat sound
ctrL=ctrR=0

while 1 :
	_,frame = cap.read()

	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	#Create drum stick tip mask and dilate it
	mask = cv2.inRange(hsv, l, u)
	mask = cv2.dilate(mask,kernel,iterations=3)
	
	#Implement beat sound control

	#Small Tom control
	if ctrL==0:
		if (mask[370:410,420:560]).any():
			winsound.PlaySound("SmallTom", winsound.SND_FILENAME)
			ctrL=1
		
	if ctrL==1 and not ((mask[370:410,100:240]).all()):
		ctrL=0

	#Snare control
	if ctrR==0:
		if (mask[370:410,100:240]).any():
			winsound.PlaySound("Snare", winsound.SND_FILENAME)
			ctrR=1
		
	if ctrR==1 and not ((mask[370:410,100:240]).all()):
		ctrR=0


	#LEFT DRUM
	cv2.rectangle(frame,(420,410),(560,370),(42,42,165),-1)
	cv2.rectangle(frame,(410,400),(570,380),(0,0,0),-1)
	
	#RIGHT DRUM
	cv2.rectangle(frame,(100,410),(240,370),(42,42,165),-1)
	cv2.rectangle(frame,(90,400),(250,380),(0,0,0),-1)

	#Flip the image to get mirror image
	flip_frame = np.flip(frame,1) #'1' > vertical axis; flips the image matrix about this axis
	flip_mask = np.flip(mask,1)

	#Display the drums
	cv2.imshow('Aerodrums',flip_frame)

	if cv2.waitKey(1) == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
