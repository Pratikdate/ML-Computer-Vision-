import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('coca cola.jpeg')

imgray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imblure=cv.GaussianBlur(imgray,(9,9),6)

imgcanny=cv.Canny(img,150,260)
imgdilation=cv.dilate(imgcanny,kernel=np.ones((5,5),np.uint8),iterations=2)
imgerode=cv.erode(imgcanny,kernel=np.ones((5,5),np.uint8))



cv.imshow("display",imgcanny)
cv.imshow("dilation",imgdilation)
cv.imshow("dilati",imgerode)
cv.waitKey(0)