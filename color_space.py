import cv2

IMAGES_RGB = './images/rgb.png'

input_image = cv2.imread(IMAGES_RGB)


B, G, R = input_image[257, 20]
print(B)
print(G)
print(R)
print("Color image shape {}".format(input_image.shape))

gray_img = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
print("Gray image shape {}".format(gray_img.shape))
print("Gray image pixel value at 10x50 = {}".format(gray_img[10, 50]))

print(input_image)
''''
# Color image shape (270, 535, 3)
for i in range(270):
	for j in range(535):
		B, G, R = input_image[i, j]
		if B != 255:
			print(B, G, R, i, j)
			break
	print()
'''
	
'''
cv2.imshow('Input Image', input_image)


cv2.waitKey()
cv2.destroyAllWindows()
'''