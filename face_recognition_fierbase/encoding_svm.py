import cv2 as cv 
import face_recognition
import pickle
import os
import tensorflow as tf
import keras
import matplotlib.pyplot as plt 
import pandas as pd 

import numpy as np
from sklearn.svm  import SVC

foldermodelpath="project_product\img"
pathlist=os.listdir(foldermodelpath)
imgpathlist=[]

stdID=[]

for path in pathlist:
    imgpathlist.append(cv.imread(os.path.join(foldermodelpath,path)))
    stdID.append(os.path.splitext(path)[0])



def findencoding(imagelist):
    encode_list=[]
    for img in imagelist:
        img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        
        encode_list.append(encode)
    
    return encode_list



def x_train_y_train(img_path='project_product\img'):
    pathlist=os.listdir(img_path)
    pathlist_img=[]
    y_lable=[]
   
    x_feature=[]


    for path in pathlist:
        img=cv.imread(os.path.join(img_path,path))
        imgs = cv.resize(img,(178,218),interpolation = cv.INTER_AREA)    
        imgs = imgs.reshape(1,218,178,3)
        x_feature.append(imgs)
        


        pathlist_img.append(os.path.join(img_path,path))
        lable=int(os.path.splitext(path)[0])
        
        y_lable.append(lable)
    x_feature=findencoding(x_feature)
    
    return pathlist_img,x_feature,y_lable


def model(x,y):
    
    model=SVC(C=1,kernel="poly")
    model.fit(x,y)
    return model



pathlist_img,x,y=x_train_y_train()

cv.imshow('img',x[0][0])

cv.waitKey(0)


svm_m=model(x,y)

print(svm_m.fit_status_)

filename = 'nn_encode_model.sav'
pickle.dump((svm_m,pathlist_img,y), open(filename, 'wb'))


def test(img,model):
    
    preo=model.predict(img)

       
    return preo

img=cv.imread("project_1\img\123#elon.jpg")

#pre=test(x,svm_m)
#print(pre)



'''

def findencoding(imagelist):
    encode_list=[]
    model=tf.keras.applications.NASNetMobile(include_top=False,input_shape=(h,w,3),weights='imagenet')
    model.trainable = False
    flat=keras.layers.Flatten()(model.layers[-1].output)
    dence1=keras.layers.Dense(256,activation='relu')(flat)

    model=tf.keras.models.Model(inputs=(model.inputs),outputs=(dence1))
    encode=model.predict(imagelist)
    
    
    encode_list.append(encode)
    encode_img=np.array(encode)
    encode_img=encode_img.reshape(len(imagelist),256)

    return encode_img
'''

#encode=findencoding(X)