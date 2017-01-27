import cv
import numpy as np




orig = cv.LoadImage('image4_with_sample.jpg')

grey_scale = cv.CreateImage(cv.GetSize(orig), 8, 1)
processed = cv.CreateImage(cv.GetSize(orig), 8, 1)

cv.Smooth(orig, orig, cv.CV_GAUSSIAN, 5, 5)
cv.CvtColor(orig, grey_scale, cv.CV_RGB2GRAY)
cv.Erode(grey_scale, processed, None, 10)
cv.Dilate(processed, processed, None, 10)
cv.Canny(processed, processed, 5, 70, 3)
cv.Smooth(processed, processed, cv.CV_GAUSSIAN, 15, 15)

cv2.imwrite('sample_after_smoothing.jpg',processed)

storage = cv.CreateMat(orig.width, 1, cv.CV_32FC3)


cv.HoughCircles(processed, storage, cv.CV_HOUGH_GRADIENT, 1, 16.0, 10, 140)

for i in range(0, len(np.asarray(storage))):
    print "circle #%d" %i
    Radius = int(np.asarray(storage)[i][0][2])
    x = int(np.asarray(storage)[i][0][0])
    y = int(np.asarray(storage)[i][0][1])
    center = (x, y)
    print x,y

    cv.Circle(orig, center, 1, cv.CV_RGB(0, 255, 0), 1, 8, 0)
    cv.Circle(orig, center, Radius, cv.CV_RGB(255, 0, 0), 1, 8, 0)

    cv.Circle(processed, center, 1, cv.CV_RGB(0, 0, 0), -1, 8, 0)
    cv.Circle(processed, center, Radius, cv.CV_RGB(255, 0, 0), 3, 8, 0)

cv2.imwrite('circle_coordinates.jpg',processed)
