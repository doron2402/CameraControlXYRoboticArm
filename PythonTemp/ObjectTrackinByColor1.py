import cv2
import numpy as np




def main():
    # Take a frame
    image = cv2.imread('image2_with_sample.jpg')
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    '''#---------Detect Blue Objects-------------
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #Bitwise-AND mask and original image
    res = cv2.bitwise_and(image,image, mask = mask)

    cv2.imwrite('image4_blue_result.jpg',res)
    */'''

    #---------Detect Red Objects-------------
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
    
    

    cv2.imwrite('image2_red_result.jpg',res2)
    

if (__name__ == "__main__"):
	main()