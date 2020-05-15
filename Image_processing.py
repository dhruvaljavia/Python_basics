import cv2

img = cv2.imread('me.jpg',1)
rd = cv2.imread('road.jpeg',1)

# cv2.imwrite('resizedme.jpg',img)

img = cv2.resize(img, (660,512))
rd = cv2.resize(rd, (660,512))

img = cv2.rectangle(img, (100,100),(200,200),(255,0,0),-1) #img,topleftcorner,bottomrightcorner,colourBGR,-1 for filled and +ve for thickness
img = cv2.circle(img, (150,150),70,(0,255,255),5) # img, centre, radius, ...

# b,g,r=cv2.split(img)
# cv2.imshow('me in blue', b)
# cv2.imshow('me in green', g)
# cv2.imshow('me in red', r)
# mrg = cv2.merge((b,g,r))
# cv2.imshow('me in blue+green+red', mrg)

# cv2.imshow('me',img)

add1 = cv2.addWeighted(img,0.2,rd,0.8,0)
add2 = cv2.addWeighted(img,0.2,rd,0.8,100)
cv2.imshow('added1', add1)
cv2.imshow('added2', add2)

print(img[400][600][2]) #img is 3d list or array(512x660x3); width 3 is due to BGR channels
print(img.shape) # Prints dimensions as a tuple

cv2.waitKey(0)
cv2.destroyAllWindows() #destroys all windows
 
#The argument to waitKey() is a number of milliseconds to wait for keyboard input.
#The return value is either -1 (meaning no key has been pressed) or an ASCII keycode,
#such as 27 for Esc. 0 indicates "wait forever"