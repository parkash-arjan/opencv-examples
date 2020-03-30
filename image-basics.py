import cv2

input_image = cv2.imread('./images/rgb.png')
cv2.imshow('Input Image', input_image)

print(input_image.shape)

print('Height of Image:', int(input_image.shape[0]), 'pixels')
print('Width of Image: ', int(input_image.shape[1]), 'pixels')

cv2.imwrite('copy_of_rgb.jpg', input_image)
cv2.imwrite('copy_of_rgb.png', input_image)

cv2.waitKey()
cv2.destroyAllWindows()

