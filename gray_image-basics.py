import cv2

input_image = cv2.imread('./images/rgb.png')
cv2.imshow('Input Image', input_image)

gray_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayscale Image', gray_image)


cv2.waitKey()
cv2.destroyAllWindows()

