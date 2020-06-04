import cv2
import numpy as np
import math

#Setting the webcam and drawing board
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
brd = np.ones((720,1280,3),np.uint8)*255

#Defining the kernel and detecting colour HSV ranges
l = np.array([0,237,132])
u = np.array([21,255,255])
kernel = np.ones((7,7),np.uint8)

#Defining global variables
r = c = 0
rad = 5
clr = (0,0,255)
ctrl = 0
save = 0


while(True):
	#Getting the mask for brush tip
	_, frame = cap.read() 
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, l, u)
	mask = cv2.dilate(mask,kernel,iterations=3)

	#Classifying the input key command from user 
	key = cv2.waitKey(1)
	if key == ord('1'):
		rad = 5
	if key == ord('2'):
		rad = 8
	if key == ord('3'):
		rad = 11
	if key == ord('4'):
		rad = 14

	if key == ord('r'):
		clr = (0,0,255)
	if key == ord('g'):
		clr = (0,255,0)
	if key == ord('b'):
		clr = (255,0,0)
	if key == ord('c'):
		clr = (255,255,0)
	if key == ord('y'):
		clr = (0,255,255)
	if key == ord('p'):
		clr = (255,0,255)

	if key == ord('d'):
		ctrl = 1
	if key == ord('s'):
		ctrl = 0

	if key == ord('z'):
		save = 1

	#Getting the mean central position of the brush tip
	x = np.nonzero(np.int32(mask))
	size = np.size(x)/2
	if(size != 0):
		r = math.floor(np.sum(x[0][:])/size)
		c = math.floor(np.sum(x[1][:])/size)

	#Drawing the tracker circle and colour disc
	drw = np.ones((720,1280,3),np.uint8)*255
	drw = cv2.circle(drw, (c,r),rad,clr,-1)

	pntr = np.ones((720,1280,3),np.uint8)*255
	pntr = cv2.circle(pntr, (c,r),rad+5,(0,0,0),2)

	#Displaying the drawing
	if ctrl == 1:
		brd = cv2.circle(brd, (c,r),rad,clr,-1)
		flip = np.flip(cv2.bitwise_and(pntr,brd),1)
		flip = cv2.putText(flip, "d -> start drawing   s -> stop drawing", (5,15), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
		flip = cv2.putText(flip, "1 - 4 -> brush sizes   b -> blue  g -> green  r -> red  y -> yellow  c -> cyan  p -> purple", (5,30), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
		flip = cv2.putText(flip, "z -> save drawing   q -> quit", (5,45), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
		flip = cv2.putText(flip, "Detecting colour : ", (1100,15), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
		flip = cv2.rectangle(flip, (1220,5),(1240,25),(17,183,255),-1)
		cv2.imshow('Drawing board', flip)
	if ctrl == 0:
		flip = np.flip(cv2.bitwise_and(pntr,cv2.bitwise_and(drw,brd)),1)
		flip = cv2.putText(flip, "d -> start drawing   s -> stop drawing", (5,15), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
		flip = cv2.putText(flip, "1 - 4 -> brush sizes   b -> blue  g -> green  r -> red  y -> yellow  c -> cyan  p -> purple", (5,30), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)
		flip = cv2.putText(flip, "z -> save drawing   q -> quit", (5,45), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)		
		flip = cv2.putText(flip, "Detecting colour : ", (1100,15), cv2.FONT_HERSHEY_DUPLEX, 0.4, (0,0,0), 1, cv2.LINE_AA)		
		flip = cv2.rectangle(flip, (1220,5),(1240,25),(17,183,255),-1)
		cv2.imshow('Drawing board',flip)

	#Saving the drawing on user's command
	if save == 1:
		cv2.imwrite('drawing.jpg', np.flip(brd,1))
		save = 0

	if key == ord('q'):
		break
	
cap.release()
cv2.destroyAllWindows()
