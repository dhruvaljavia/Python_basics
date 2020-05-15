import cv2

def fun(arr):
	b,g,r = cv2.split(arr)
	b=(b*4)%255
	g=(g*1)%255
	r=(r*2)%255
	mrg=cv2.merge((b,g,r))
	return mrg

img = cv2.resize(cv2.imread('me.jpg',1),(660,512))
funimg=fun(img)
cv2.imshow('me',img)
cv2.imshow('funme',funimg)
add=cv2.addWeighted(img,0.7,funimg,0.3,0)
cv2.imshow('addfunme',add)

cv2.waitKey(0)
cv2.destroyAllWindows()
