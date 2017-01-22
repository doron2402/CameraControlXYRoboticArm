import cv2
import numpy as np




def main():
    # Take a frame
    image = cv2.imread('image1_with_sample.jpg')
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    #lower_blue = np.array([110,50,50])
    #upper_blue = np.array([130,255,255])
    # define range of red color in HSV
    lower_red = np.array([190,50,60])
    upper_red = np.array([255,50,0])
    # Threshold the HSV image to get only blue colors
    #mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.inRange(hsv, lower_red, upper_red)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(image,image, mask = mask)
    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    #cv2.imshow('res',res)
    cv2.imwrite('image1_red_result.jpg',res)
    

if (__name__ == "__main__"):
	main()