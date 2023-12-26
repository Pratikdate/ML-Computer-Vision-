import cv2 as cv 
import numpy as np
import tensorflow as tf 
import matplotlib.pyplot as plt
from sklearn.feature_extraction import image

cap =cv.VideoCapture(0)

model=tf.keras.models.load_model("VGG16_face_bbox_feture_detection.h5")

w,h=178,218

while True:
    succ,img=cap.read()
    #img=cv.imread('project_product\img\012.jpg')
    
    
    #img=image.copy()
    imgpa= cv.resize(img,(300,300),interpolation = cv.INTER_AREA)
    patches = image.extract_patches_2d(imgpa, (300,300))
    print(patches.shape)
    for imgp in patches:
        imgsh= cv.resize(imgp,(w,h),interpolation = cv.INTER_AREA)
        imgsh = imgsh.reshape(h,w,3)


        
        img = cv.resize(imgp,(178,218))    
        #img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        imgs = img.reshape(1,218,178,3)

        
        
        var=model.predict(imgs)
        print(var)
        
        
        x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,_,_=var[0]
        cv.rectangle(img,(int(x1*w),int(y1*h)),(int(x2*w),int(y2*h)),(0,255,0),1,cv.LINE_AA)
        cv.rectangle(img,(int(x3*w),int(y3*h)),(int(x4*w),int(y4*h)),(0,255,0),1,cv.LINE_AA)
        cv.rectangle(img,(int(x5*w-5),int(y5*h)-20),(int(x6*w)+6,int(y6*h)+8),(0,255,0),1,cv.LINE_AA)
        
        print((int(x1*w),int(y1*h)),(int(x2*w),int(y2*h)))
        
        #imgnew= imgs.reshape(218,178,3)





        cv.imshow('img',img)
        if cv.waitKey(1)==ord('q'):
            break