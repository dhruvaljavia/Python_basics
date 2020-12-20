import cv2

img = cv2.imread('my_photo.jpg',1)
cv2.imshow('photo',img)

re_img = cv2.resize(img, (200,260))

cv2.imshow('resized_photo',re_img)
cv2.waitKey(0)

cv2.imwrite('resized_my_photo.jpg',re_img)