import cv2 as cv
import numpy as np

img = cv.imread('images/quadra.jpeg')

resized = cv.resize(img, (400, 300))
cv.imshow('Resized Image', resized)

def translate(img, x, y):
    transMat = np.float32([[1, 0 ,x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
# -x --> Left
# +x --> Right
# -y --> Up
# +y --> Down 



translated = translate(resized, -100, 100)
cv.imshow('Translated Image', translated)

# Rotation
# def rotate(img, angle, rotPoint=None):
#     (h, w) = img.shape[:2]

#     if rotPoint is None:
        

cv.waitKey(0)
cv.destroyAllWindows()