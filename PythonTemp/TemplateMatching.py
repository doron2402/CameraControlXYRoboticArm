import cv2
import numpy as np
     
     
img = cv2.imread('image4_with_sample.jpg',0)
img2 = img.copy()
template = cv2.imread('red circle.jpg',0)
w, h = template.shape[::-1]
     
# All the 6 methods for comparison in a list
#methods = ['cv2.TM_CCOEFF']
    
img = img2.copy()
#method = eval(methods)
    
# Apply template Matching
res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
   
    
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)
    
cv2.rectangle(img,top_left, bottom_right, 255, 2)

cv2.imwrite('Matching Result.jpg',res)
cv2.imwrite('Detected Point.jpg',img)
    