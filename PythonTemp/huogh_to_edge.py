import cv2
import numpy as np




def main():
    # Take a frame
    image = cv2.imread('two circles.png')
    image2 = image.copy()
    # Convert BGR to HSV
    hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
    

    #---------Detect Red Objects-------------
    # define range of red color in HSV
    lower_red = np.array([0,70,50])
    upper_red = np.array([10,255,255])
    # Threshold the HSV image to get only red colors
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    # Bitwise-AND mask and original image
    #res = cv2.bitwise_and(image,image, mask = mask)

    lower_red = np.array([175,70,50])
    upper_red = np.array([180,255,255])
    
    mask2 = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.bitwise_or(mask1, mask2, mask = None)
    #res2 = cv2.bitwise_and(image,image, mask = mask)
    
    #res3= cv2.bitwise_or(image,image, mask = mask)
    #---------Detect edge-------------
    #edge = cv2.Canny(res3,100,200)

    cv2.imwrite('two circles result.png',mask)
    img2 = cv2.imread('two circles result.png',0)
    #---------Detect circle-------------
    img2 = cv2.medianBlur(img2,5)


    circles = cv2.HoughCircles(img2,cv2.HOUGH_GRADIENT,1,40, param1=35,param2=20,minRadius=0,maxRadius=0)
    #circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,10, param1=100,param2=30,minRadius=5,maxRadius=50)
    
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