import cv2
import datetime

cap = cv2.VideoCapture(0) # 0 for the laptop cam
# fourcc = cv2.VideoWriter_fourcc(*'H264') # H264 is codec for mp4, XVID for avi
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480)) # 20 is frame rate per sec. (640,480) is frame size

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(True):
    _, frame = cap.read() # _(ret) store True if a frame is read otherwise False 
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converts BGR frame to GRAYSCALE frame

    datet = str(datetime.datetime.now())
    frame = cv2.putText(frame, datet, (10,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2, cv2.LINE_AA)

    cv2.imshow('camera', frame)
    # out.write(gray) # writes 'gray' frame to output.mp4
    if cv2.waitKey(1)==ord('q'):
        break
    
cap.release()
# out.release()
cv2.destroyAllWindows()
