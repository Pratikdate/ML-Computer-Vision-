import cv2 as cv
import numpy as np

height,width=900,300


img=cv.imread("coca cola.jpeg")
pts1=np.float32([[475,152],[165,136],[93,706],[465,714]])

pts2=np.float32([[0,0],[height,0],[0,width],[height,width]])

matrix=cv.getPerspectiveTransform(pts1,pts2)
imgout=cv.warpPerspective(img,matrix,(width,height))

cv.imshow("img",imgout)
cv.waitKey(0)