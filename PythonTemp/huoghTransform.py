import cv2
import numpy as np

img = cv2.imread('image4_with_sample.jpg')
img3 = img.copy()

img2 = cv2.medianBlur(img,5)

gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

cimg = cv2.filter2D(gray, cv2.CV_8U, gb_kernel.transpose())

circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
	cv2.circle(img3,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
	cv2.circle(img3,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',img3)
cv2.waitKey(0)
cv2.destroyAllWindows()