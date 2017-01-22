 import cv2
import numpy as np




def main():
    # Take a frame
    image = cv2.imread('image4_with_sample.jpg')
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    #---------Detect Blue Objects-------------
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #Bitwise-AND mask and original image
    res = cv2.bitwise_and(image,image, mask = mask)

    cv2.imwrite('image4_blue_result.jpg',res)
    cv2.imwrite('image4_mask_result.jpg',res)

    #Hough Line Transform
    # detect circles in the image
    circles = cv2.HoughCircles(mask, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)
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
 
	# show the output image
    cv2.imwrite('image4_output.jpg',output)
	
    

    '''#---------Detect Red Objects-------------
    # define range of red color in HSV
    lower_red = np.array([0,70,50])
    upper_red = np.array([10,255,255])
    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(image,image, mask = mask)

    lower_red = np.array([175,70,50])
    upper_red = np.array([180,255,255])
    
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res2 = cv2.bitwise_and(image,image, mask = mask)
    
    res3= cv2.bitwise_or(image,image, mask = mask)

    cv2.imwrite('image4_red_result.jpg',res3)
    */'''

if (__name__ == "__main__"):
	main()