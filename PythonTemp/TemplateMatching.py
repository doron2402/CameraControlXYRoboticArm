import cv2
import numpy as np
     
     
img = cv2.imread('image2_with_sample.jpg')

template = cv2.imread('blue circle.jpg',0)
w, h = template.shape[::-1]

     
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#---------Detect Blue Objects-------------
# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
#Bitwise-AND mask and original image
res = cv2.bitwise_and(img,img, mask = mask)
img = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
 
cv2.imwrite('Proccess img.jpg',img)

# Apply template Matching
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
   
    
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
    
cv2.rectangle(img,top_left, bottom_right, 255, 2)

cv2.imwrite('Matching Result.jpg',res)
cv2.imwrite('Detected Point.jpg',img)
    