import cv2 as cv 
import numpy as np



cap =cv.VideoCapture(0)


def preprocessing(img):
    imgray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgblure=cv.GaussianBlur(imgray,(7,7),1)
    imgcanny=cv.Canny(imgblure,180,180)
    #kernel=np.ones((5,5))
    #dilation=cv.dilate(imgcanny,kernel,iterations=2)
    #imgther=cv.erode(dilation,kernel,iterations=1)

    return imgcanny



def getcontours(cm_per_pixel_height,cm_per_pixel_width,img):
    #img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgcounter=preprocessing(img)
    contours,hierachy=cv.findContours(imgcounter,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    height_cm,width_cm=0,0
    for cnt in contours:
        area=cv.contourArea(cnt)
        if area >0:
            cv.drawContours(imgcounter,cnt,-1,(0,255,0),3)
            
            
            per1=cv.arcLength(cnt,True)
            
            approx=cv.approxPolyDP(cnt,0.04*per1,True)
            x, y, w, h = cv.boundingRect(approx)
            cv.rectangle(imgcounter,(x,y),(x+w,y+h),(0,255,1),2)
            height_cm=cm_per_pixel_height*h
            width_cm=cm_per_pixel_width*w
            cv.imshow("counter",imgcounter)
    return height_cm,width_cm,x,y,w,h
        
def find_pixel_per_cm(bg_height,bg_width):
    shape=img.shape
    cm_per_pixel_height=bg_height/shape[0]
    cm_per_pixel_width=bg_width/shape[1]
    return cm_per_pixel_height,cm_per_pixel_width



def draw_arrow(height_cm,width_cm,x,y,w,h):
    cv.arrowedLine(img,(x,y),(x+w,y+h),(0,255,0),2,cv.LINE_4)
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,f"{height_cm}cm",(x-30,y+60),font,1,(0,255,0),1,cv.LINE_4)
    
    cv.putText(img,f"{width_cm}cm " ,(x,y+60),font,1,(0,255,0),1,cv.LINE_4)
            
    return img
            
            
            
                





while True:
    succ,image=cap.read()
    img=image.copy()
    
    bg_height=420
    bg_width=600
    cm_per_pixel_height,cm_per_pixel_width=find_pixel_per_cm(bg_height,bg_width)

    height_cm,width_cm,x,y,w,h=getcontours(cm_per_pixel_height,cm_per_pixel_width,img)
    img=draw_arrow(str(np.float16(height_cm)),str(np.float16(width_cm)),x,y,w,h)
    
    print(x,y)





    cv.imshow("img",img)
    if cv.waitKey(1)==ord('q'):
        break