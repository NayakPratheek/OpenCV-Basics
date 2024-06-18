import cv2

img = cv2.imread('cypher.jpg', 1)   # 0 for grayscale    # 1 for color      # -1 for alpha channel

img = cv2.resize(img, (500, 500))       #to resize the output window

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)      #to rotate the output windpw

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()