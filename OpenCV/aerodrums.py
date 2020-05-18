import cv2
import numpy as np
import winsound
import threading
# CAP_PROP_FRAME_HEIGHT = 540
# CAP_PROP_FRAME_WIDTH = 960

def playDrumL():

	#Define kernel for dilation of drum stick tip
	kernel = np.ones((7,7),np.uint8)

	#HSV ranges for detecting drum stick tip
	l = np.array([0,237,132])
	u = np.array([21,255,255])

	#Control for beat sound
	ctrl=ctrtl=ctrm=ctrc=ctrhho=0

	while 1 :
		_,PFRAME = cap.read()
		hsv = cv2.cvtColor(PFRAME, cv2.COLOR_BGR2HSV)

		#Create drum stick tip mask and dilate it
		mask = cv2.inRange(hsv, l, u)
		mask = cv2.dilate(mask,kernel,iterations=3)

		#Implement beat sound control

		#control
		if ctrl==0:
			if (mask[440:480,570:710]).any():
				winsound.PlaySound("Snare", winsound.SND_FILENAME)
				ctrl=1
			
		if ctrl==1 and (not (mask[440:480,570:710]).any()):
			ctrl=0

		if ctrtl==0:
			if (mask[250:290,500:640]).any():
				winsound.PlaySound("SmallTom_short", winsound.SND_FILENAME)
				ctrtl=1
			
		if ctrtl==1 and (not (mask[250:290,500:640]).any()):
			ctrtl=0

		if ctrm==0:
			if (mask[440:480,360:500]).any():
				winsound.PlaySound("BassDrum_short", winsound.SND_FILENAME)
				ctrm=1
			
		if ctrm==1 and (not (mask[440:480,360:500]).any()):
			ctrm=0

		if ctrc==0:
			if (mask[100:120,710:870]).any():
				winsound.PlaySound("Crash_short", winsound.SND_FILENAME)
				ctrc=1
			
		if ctrc==1 and (not (mask[100:120,710:870]).any()):
			ctrc=0

		if ctrhho==0:
			if (mask[290:300,760:920]).any():
				winsound.PlaySound("HHopen_short", winsound.SND_FILENAME)
				ctrhho=1
			
		if ctrhho==1 and (not (mask[290:300,760:920]).any()):
			ctrhho=0
	
def playDrumR():

	#Define kernel for dilation of drum stick tip
	kernel = np.ones((7,7),np.uint8)

	#HSV ranges for detecting drum stick tip
	l = np.array([0,237,132])
	u = np.array([21,255,255])

	#Control for beat sound
	ctrr=ctrtr=ctrri=ctrhhc=0

	while 1 :
		_,PFRAME = cap.read()
		hsv = cv2.cvtColor(PFRAME, cv2.COLOR_BGR2HSV)

		#Create drum stick tip mask and dilate it
		mask = cv2.inRange(hsv, l, u)
		mask = cv2.dilate(mask,kernel,iterations=3)

		#Implement beat sound control

		#control
		if ctrr==0:
			if (mask[440:480,150:290]).any():
				winsound.PlaySound("FloorTom", winsound.SND_FILENAME)
				ctrr=1
			
		if ctrr==1 and (not (mask[440:480,150:290]).any()):
			ctrr=0

		if ctrtr==0:
			if (mask[250:290,220:360]).any():
				winsound.PlaySound("MedTom_short", winsound.SND_FILENAME)
				ctrtr=1
			
		if ctrtr==1 and (not (mask[250:290,220:360]).any()):
			ctrtr=0

		if ctrri==0:
			if (mask[100:120,110:270]).any():
				winsound.PlaySound("Ride", winsound.SND_FILENAME)
				ctrri=1
			
		if ctrri==1 and (not (mask[100:120,110:270]).any()):
			ctrri=0

		if ctrhhc==0:
			if (mask[440:450,760:920]).any():
				winsound.PlaySound("HHclose_long", winsound.SND_FILENAME)
				ctrhhc=1
			
		if ctrhhc==1 and (not (mask[440:450,760:920]).any()):
			ctrhhc=0


def dispDrum():

	while 1 :
		_,DFRAME = cap.read()

		#LEFT DRUM
		cv2.rectangle(DFRAME,(570,480),(710,440),(42,42,165),-1)
		cv2.rectangle(DFRAME,(560,470),(720,450),(0,0,0),-1)

		#RIGHT DRUM
		cv2.rectangle(DFRAME,(150,480),(290,440),(42,42,165),-1)
		cv2.rectangle(DFRAME,(140,470),(300,450),(0,0,0),-1)

		#TOPLEFT DRUM
		cv2.rectangle(DFRAME,(500,290),(640,250),(42,42,165),-1)
		cv2.rectangle(DFRAME,(490,280),(650,260),(0,0,0),-1)

		#TOPRIGHT DRUM
		cv2.rectangle(DFRAME,(220,290),(360,250),(42,42,165),-1)
		cv2.rectangle(DFRAME,(210,280),(370,260),(0,0,0),-1)

		#MID DRUM
		cv2.rectangle(DFRAME,(360,480),(500,440),(42,42,165),-1)
		cv2.rectangle(DFRAME,(350,470),(510,450),(0,0,0),-1)

		#CRASH
		cv2.rectangle(DFRAME,(710,120),(870,110),(0,0,0),-1)

		#RIDE
		cv2.rectangle(DFRAME,(110,120),(270,110),(0,0,0),-1)

		#HHOPEN
		cv2.rectangle(DFRAME,(760,300),(920,290),(0,0,0),-1)

		#HHCLOSE
		cv2.rectangle(DFRAME,(760,450),(920,440),(0,0,0),-1)


		#Flip the image to get mirror image
		flip_frame = np.flip(DFRAME,1) #'1' > vertical axis; flips the image matrix about this axis
		#flip_mask = np.flip(mask,1)

		#Put text on the image
		flip_text_frame = cv2.putText(flip_frame, "Aero-Drums", (380,40), cv2.FONT_HERSHEY_DUPLEX, 1, (255,255,255), 2, cv2.LINE_AA)
		flip_text_frame = cv2.putText(flip_text_frame, "Press 'Q' to quit", (10,520), cv2.FONT_ITALIC, 0.5, (255,255,255), 1, cv2.LINE_AA)

		#framelay the drums
		cv2.imshow('Aerodrums',flip_text_frame)
		#cv2.imshow('mask',flip_mask)

		if cv2.waitKey(1) == ord('q'):
			break


cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 540)

td = threading.Thread(target=dispDrum)
tpl = threading.Thread(target=playDrumL)
tpr = threading.Thread(target=playDrumR)

tpl.setDaemon(True)
tpr.setDaemon(True)

td.start()
tpl.start()
tpr.start()

cv2.destroyAllWindows()