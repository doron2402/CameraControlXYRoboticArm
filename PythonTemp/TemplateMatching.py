import cv2
import numpy as np
     
     
img = cv2.imread('image2_with_sample.jpg')

template = cv2.imread('blue circle.jpg',0)
w, h = template.shape[::-1]


     
hsv = cv2.cvtColor(img2,cv2.COLOR_BGR2HSV)
#---------Detect Blue Object-------------
img2=img.copy()
# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])
# Threshold the HSV image to get only blue colors
mask = cv2.inRange(hsv, lower_blue, upper_blue)
#Bitwise-AND mask and original image
res = cv2.bitwise_and(img2,img2, mask = mask)
img2 = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
 
cv2.imwrite('Proccess img.jpg',img)

# Apply template Matching
res = cv2.matchTemplate(img2,template,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    
top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

x = top_left[0] + w/2
y = top_left[1] + h/2

blue_coor = [x,y]
print ("X=",blue_coor[0],"Y=",blue_coor[1])

    
cv2.rectangle(img,top_left, bottom_right, 255, 2)

#---------Detect Red Object-------------
img2=img.copy()
# define range of blue color in HSV
lower_red = np.array([0,70,50])
upper_red = np.array([10,255,255])
# Threshold the HSV image to get only red colors
mask = cv2.inRange(hsv, lower_red, upper_red)
#Bitwise-AND mask and original image
res = cv2.bitwise_and(img2,img2, mask = mask)
img2 = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
 
cv2.imwrite('Proccess img.jpg',img)

# Apply template Matching
res = cv2.matchTemplate(img2,template,cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    
top_left = min_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

x = top_left[0] + w/2
y = top_left[1] + h/2

blue_coor = [x,y]
print ("X=",red_coor[0],"Y=",red_coor[1])

    
cv2.rectangle(img,top_left, bottom_right, 255, 2)

#---------Save image-------------
cv2.imwrite('Detected Point.jpg',img)

  