import cv2

image = cv2.imread('static/b1.jpg')
mask = cv2.imread('static/b2.png', 0)
mask = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
image[mask==255] = (36,255,12)
#255,12,5
#36,255,12
cv2.imshow('image', image)
cv2.imshow('mask', mask)
cv2.waitKey()
