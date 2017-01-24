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
    BinaryImg = cv2.inRange(hsv, lower_blue, upper_blue)
    #Bitwise-AND mask and original image
    #res = cv2.bitwise_and(image,image, mask = mask)

    cv2.imwrite('image4_mask_result.jpg',BinaryImg)

    circles = cv2.HoughCircles(BinaryImg,cv2.HOUGH_GRADIENT,1,20, 
        param1=50,param2=30,minRadius=0,maxRadius=0)

    
    print (circles)
    

if (__name__ == "__main__"):
    main()