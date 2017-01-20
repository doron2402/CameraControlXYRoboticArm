import cv2

def main():
	image = cv2.imread('pic_mountain.jpg')
	gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	cv2.imwrite('gray_image.png',gray_image)

if (__name__ == "__main__"):
	main()