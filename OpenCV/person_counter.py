import cv2
import numpy as np

cap = cv2.VideoCapture(700)
# CAP_PROP_FRAME_HEIGHT = 480
# CAP_PROP_FRAME_WIDTH = 640
ctr = 1
thresh = 200
cL=cR=cLX=cRX=0
flgL=flgR=0

cv2.waitKey(2000)
_,init = cap.read()
B,G,R = cv2.split(init)
Rline = np.int32(B[0:480,180:190])
Lline = np.int32(B[0:480,450:460])
cv2.waitKey(2000)

while 1:
	_,frame = cap.read()
	
	b,g,r = cv2.split(frame)
	cRline = np.int32(b[0:480,180:190])
	cLline = np.int32(b[0:480,450:460])

	diffR = np.abs(cRline - Rline)
	diffL = np.abs(cLline - Lline)

	if np.any(diffR>thresh): 
		if cL==0 and flgR==0:
			print(str(ctr)+' >>crossed from right!')
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
			print(str(ctr)+' >>crossed from left!')	
			cL=1
			flgL=1
		elif cR==1:
			cLX=1

	if not np.any(diffL>thresh) and cLX==1:
		cLX = 0
		cL = cR = 0
		flgR = flgL = 0
		

	cv2.rectangle(frame,(180,480),(190,0),(0,0,0),-1)
	cv2.rectangle(frame,(450,480),(460,0),(0,0,0),-1)
	fframe = np.flip(frame,1)

	cv2.imshow('webcam_feed',fframe)
	cv2.imshow('gray',np.flip(b,1))

	if cv2.waitKey(1) == ord('q'):
		break

	ctr = ctr + 1

cap.release()
cv2.destroyAllWindows()