import cv2
import numpy as np

img = cv2.imread('two circles.png',0)

#some comment
img = cv2.medianBlur(img,5)

cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

#cimg = cv2.filter2D(gray, cv2.CV_8U, gb_kernel.transpose())

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,40, param1=35,param2=20,minRadius=0,maxRadius=0)
#circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10, param1=100,param2=30,minRadius=5,maxRadius=50)
if circles is None:
	print "No circle found"

else:
	print circles
	circles = np.uint16(np.around(circles))
	for i in circles[0,:]:
    	# draw the outer circle
		cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    	# draw the center of the circle
		cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

	
	cv2.imwrite('detected circles.jpg',cimg)

