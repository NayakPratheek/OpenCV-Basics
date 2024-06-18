import cv2

img = cv2.imread('cypher.jpg', 1)


tag = img[100:300, 500:800]
img[100:300, 650:950] = tag

img = cv2.resize(img, (600,600))

cv2.imshow('new_img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# print(img.shape)          shows th height, width and channels of the image