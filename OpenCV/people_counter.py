import cv2
import numpy as np
from datetime import datetime as DT
import os

cap = cv2.VideoCapture(700)
# CAP_PROP_FRAME_HEIGHT = 480
# CAP_PROP_FRAME_WIDTH = 640

ctr = 0 # Counter for updating the initial cross lines
thresh = 200 # For distinguishing between pixel noise and crossing person

LC=RC=0 # Variables storing no. of people crossing from left and right

cL=cR=cLX=cRX=0
flgL=flgR=0

# Sets the initial cross lines
cv2.waitKey(2000)
_,init = cap.read()
B,G,R = cv2.split(init)
Rline = np.int32(B[0:480,180:190])
Lline = np.int32(B[0:480,450:460])
cv2.waitKey(2000)

# Write the data to a file
file = open('C:\\Users\\Admin\\Python progs\\OpenCV\\people_counter_data.txt','a')
file.write('\nDATE : ' + str(DT.now())[0:10])
file.write('\nSTART TIME : ' + str(DT.now())[11:19])

# Reads and displays the web cam feed
while 1:
	ctr = ctr + 1
	_,frame = cap.read()
	
	# Extracts current cross lines from the frame
	b,g,r = cv2.split(frame)
	cRline = np.int32(b[0:480,180:190])
	cLline = np.int32(b[0:480,450:460])

	# Calculates absolute difference between current and initial cross lines
	diffR = np.abs(cRline - Rline)
	diffL = np.abs(cLline - Lline)

	# IF-ELSE contruct which determines if a person has crossed from left or right
	if np.any(diffR>thresh): 
		if cL==0 and flgR==0:
			print('crossed from right!')
			RC=RC+1
			cR=1
			flgR=1
		elif cL==1:
			cRX=1

	if not np.any(diffR>thresh) and cRX==1:
		cRX = 0
		cL = cR = 0
		flgL = flgR = 0
		

	if np.any(diffL>thresh):
		if cR==0 and flgL==0:
			print('crossed from left!')
			LC=LC+1	
			cL=1
			flgL=1
		elif cR==1:
			cLX=1

	if not np.any(diffL>thresh) and cLX==1:
		cLX = 0
		cL = cR = 0
		flgR = flgL = 0
		

	# Displays the web cam feed
	cv2.rectangle(frame,(180,480),(190,0),(0,0,0),-1)
	cv2.rectangle(frame,(450,480),(460,0),(0,0,0),-1)
	fframe = np.flip(frame,1)
	cv2.imshow('webcam_feed',fframe)
	# cv2.imshow('gray',np.flip(b,1))


	if cv2.waitKey(1) == ord('q'):
		break


	# Updates the initial cross lines after every 500 iterations(< 1 min)
	if ctr%500==0:
		if cL==0 and cR==0 and cLX==0 and cRX==0:
			Rline = np.int32(b[0:480,180:190])
			Lline = np.int32(b[0:480,450:460])
		
		ctr=0

file.write('\nEND TIME : ' + str(DT.now())[11:19])
file.write('\nNo. of people entered = ' + str(LC))
file.write('\nNo. of people left = ' + str(RC))
file.write('\nNo. of people inside the area of surveillance = ' + str(LC-RC))
file.write('\n')
file.close()

cap.release()
cv2.destroyAllWindows()
