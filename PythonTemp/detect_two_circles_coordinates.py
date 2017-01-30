import cv2
import numpy as np
from huogh_transform_function import *


def main():
    # Take a image
    image = cv2.imread('two circles.png')
    image2 = image.copy()
    #---------Detect Red Objects-------------
    r_mask = get_color_mask(image,"red")
    
    #---------Detect Red circle-------------

    circles = return_circles_values(r_mask)
    
    if circles is None:
        print "No circle found"
    else:
        print circles
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(image2,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(image2,(i[0],i[1]),2,(0,0,255),3)

    
        cv2.imwrite('detected red circles.jpg',image2)
    #---------Detect Blue Objects-------------
    b_mask = get_color_mask(image,"blue")

    #---------Detect Blue circle-------------
    circles = return_circles_values(b_mask)
    
    if circles is None:
        print "No circle found"

    else:
        print circles
        circles = np.uint16(np.around(circles))
        for i in circles[0,:]:
            # draw the outer circle
            cv2.circle(image2,(i[0],i[1]),i[2],(0,255,0),2)
            # draw the center of the circle
            cv2.circle(image2,(i[0],i[1]),2,(0,0,255),3)

    
        cv2.imwrite('detected circles.jpg',image2)

if (__name__ == "__main__"):
	main()