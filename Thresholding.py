from matplotlib import pyplot as plt
import cv2

img = cv2.imread('gradient.png', 0)

_, th1 = cv2.threshold(img, 50,128,cv2.THRESH_BINARY)     #50 > the threshold value, 128 > the maximum value which
														  #should be set to pixels exceeding threshold value(is always 255).  
														  #Pixels having below threshold value are set to 0.
														  #'img' must always be a GRAYSCALE image.
														  #First argument returns the threshold value.
_, th2 = cv2.threshold(img, 100,50,cv2.THRESH_BINARY_INV)
_, th3 = cv2.threshold(img, 127,255,cv2.THRESH_TRUNC)     
_, th4 = cv2.threshold(img, 127,255,cv2.THRESH_TOZERO)
_, th5 = cv2.threshold(img, 127,255,cv2.THRESH_TOZERO_INV)

titles = ['Image','Binary','Binary_inv','Trunc','Tozero','Tozero_inv']
images = [img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i], 'gray') # 'gray' is required here
    plt.title(titles[i])

plt.show()
