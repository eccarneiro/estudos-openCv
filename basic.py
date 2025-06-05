# import cv2 as cv


# img = cv.imread('images/quadra.jpeg')

# #Convertendo pra cinza
# #gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# #resized_image = cv.resize(img, (500, 600))
# #cv.imshow('Resized', resized_image)

# # Adicionando um Blur na imagem

# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# #cv.imshow('Blur', blur)


# # Adicionando um Canny na imagem

# canny = cv.Canny(blur, 125, 175)
# #cv.imshow('Canny', canny)

# # Dilating the image
# # dilated = cv.dilate(canny, (7, 7), iterations=3)
# # cv.imshow('Dilated', dilated)

# # Eroding the image
# # eroded = cv.erode(dilated, (7, 7), iterations=3)
# # cv.imshow('Eroded', eroded)

# # Resizing the image
# resized = cv.resize(canny, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

# # Cropping the image

# cropped = img[50:200, 200:400]
# cv.imshow('Cropped', cropped)

# cv.waitKey(0)
# cv.destroyAllWindows() 