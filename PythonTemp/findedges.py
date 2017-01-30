import cv2
import numpy as np




def main():
    # Take a frame
    image = cv2.imread('image4_with_sample.jpg')
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    

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
    
    res3= cv2.bitwise_or(image,image, mask = mask)
    
    edge = cv2.Canny(res3,100,200)

    cv2.imwrite('image4_edge_result.jpg',edge)
    

if (__name__ == "__main__"):
	main()