import cv2
import numpy as np

img = cv2.imread('image4_with_sample.jpg',0)

img1 = cv2.medianBlur(img,5)

cv2.imwrite('image4_gray_and_blur.jpg',img1)


#circles = cv2.HoughCircles(img1,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
circles = cv2.HoughCircles(img1, cv2.HOUGH_GRADIENT, 1.2, 100)


# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
 
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
        print (x)
        print (y)
        print (r)
else:
	print ("Circle not found!")

#circles = np.uint16(np.around(circles))
#for i in circles[0,:]:
    # draw the outer circle
   # cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    #cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

    #cv2.imread('detected_circles.jpg',cimg)
