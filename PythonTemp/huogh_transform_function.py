import cv2
import numpy as np


def main():
    # Take a image
    image = cv2.imread('two circles.png')
    image2 = image.copy()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    
def get_color_mask(image,color):
    #return white image with images in the color only
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    if color =='red':
        # define range of blue color in HSV
        lower_red = np.array([0,70,50])
        upper_red = np.array([10,255,255])
        # Threshold the HSV image to get only red colors
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        # define range of blue color in HSV
        lower_red = np.array([175,70,50])
        upper_red = np.array([180,255,255])
        # Threshold the HSV image to get only red colors
        mask2 = cv2.inRange(hsv, lower_red, upper_red)
        mask = cv2.bitwise_or(mask1, mask2, mask = None)

    elif color =='blue':
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

    else:
        mask = None

    return  mask

def return_circles_values(img):
    img = cv2.medianBlur(img,5)

    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,40, param1=35,param2=20,minRadius=0,maxRadius=0)
    
    if circles is None:
        print "No circle found"

    '''else:
        print circles
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(image2,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(image2,(i[0],i[1]),2,(0,0,255),3)
    '''
    return circles
    
 