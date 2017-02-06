import os
import cv2
import numpy as np




def main():
    # Take a frame
    os.system("fswebcam -r 640x480 --no-banner current_pic.jpg")
    

if (__name__ == "__main__"):
	main()