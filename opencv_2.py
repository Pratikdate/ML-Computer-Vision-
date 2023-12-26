import cv2 as cv

img=cv.imread("coca cola.jpeg")
imgresize=cv.resize(img,(100,200))

# first hight ,width
imgcrop=img[100:200,200:500]


cv.imshow('display',imgcrop)
#cv.imshow('display resize',imgresize)
print(imgresize.shape)



cv.waitKey(0)
