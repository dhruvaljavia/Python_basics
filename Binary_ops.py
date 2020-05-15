import cv2
import numpy as np

img1 = np.zeros((400,400,3),np.uint8) #np.uint8 is datatype; (400,400,3) are dimensions of 3d array or list
img1 = cv2.rectangle(img1, (100,0), (300,300), (255,255,255), -1)
img2 = np.zeros((400,400,3),np.uint8)
img2 = cv2.rectangle(img2, (100,100), (300,400), (255,255,255), -1)

AND = cv2.bitwise_and(img1, img2)
OR = cv2.bitwise_or(img1, img2)
XOR = cv2.bitwise_xor(img1, img2)
NOT = cv2.bitwise_not(XOR)

print(img1[100,150,1])

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("AND", AND)
cv2.imshow("OR", OR)
cv2.imshow("XOR", XOR)
cv2.imshow("NOTofXOR", NOT)

cv2.waitKey(0)
cv2.destroyAllWindows()
