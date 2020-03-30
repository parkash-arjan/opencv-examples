# H: 0 - 180, S: 0 - 255, V: 0 - 255
# H = Hue
# S = Saturation
# V = Value

import cv2

input_image = cv2.imread('./images/rgb.png')

hsv_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

cv2.imshow('HSV image', hsv_image)
cv2.imshow('Hue channel', hsv_image[:, :, 0])
cv2.imshow('Saturation channel', hsv_image[:, :, 1])
cv2.imshow('Value channel', hsv_image[:, :, 2])

print("HSV Image shape {}".format(hsv_image.shape))

print(hsv_image)

cv2.waitKey()
cv2.destroyAllWindows()
