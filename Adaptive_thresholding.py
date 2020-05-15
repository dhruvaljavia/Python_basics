import cv2 as cv

img = cv.imread('sudoku.jpg', 0)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,3,2) # 255 is max value
																					  # 3 is block size or the 'small region' of importance
																					  # 2 is constant 'C'
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,9,6)

cv.imshow('Image', img)
cv.imshow('th1', th1)
cv.imshow('th2', th2)
cv.imshow('th3', th3)

cv.waitKey(0)
cv.destroyAllWindows()

# If an image has different lighting conditions in different areas. In that case, adaptive thresholding can help. 
# Here, the algorithm determines the threshold for a pixel based on a small region around it. 
# So we get different thresholds for different regions of the same image which gives better results for images with varying illumination.

# In addition to the parameters of cv2.threshold, the method cv.adaptiveThreshold takes three input parameters:

# [1]The adaptiveMethod decides how the threshold value is calculated:

# cv.ADAPTIVE_THRESH_MEAN_C: The threshold value is the mean of the neighbourhood area minus the constant C.
# cv.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.

# [2]The blockSize determines the size of the neighbourhood area.
# [3]C is a constant that is subtracted from the mean or weighted sum of the neighbourhood pixels.