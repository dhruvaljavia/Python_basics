from matplotlib import pyplot as plt
import cv2

img = cv2.imread('me.jpg', 1)
img = cv2.resize(img,(660,512))
cv2.imshow('image', img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Necessary for viewing in pyplot

plt.imshow(img) # Inserts the image in window
plt.show()	# Shows the final window
			# Press 'q' to close pyplot windows

cv2.waitKey(0)
cv2.destroyAllWindows()
