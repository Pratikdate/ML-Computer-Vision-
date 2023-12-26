import cv2 as cv
import numpy as np

#img=cv.imread("coca cola.jpeg")

img=np.zeros((200,400,3),np.uint8)
#img[100:200,10:100]=255,0,0
cv.line(img,(0,0),(100,100),(0,245,0))
cv.rectangle(img,(10,10),(100,100),(0,255,255))
cv.circle(img,(100,100),20,(255,255,0))
cv.putText(img,"Hello world",(120,100),cv.FONT_ITALIC,1,(0,255,2))

cv.imshow("img",img)
cv.waitKey(0)