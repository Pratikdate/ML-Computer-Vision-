import face_recognition 
import cv2 as cv 
import os
import pickle
import numpy as np
import cvzone 
fh=438


capm=cv.VideoCapture(0)
capm.set(4,fh)
capm.set(3,640)






foldermodelpath="project_1\img"
pathlist=os.listdir(foldermodelpath)
imgpathlist=[]
imgpath=[]
for path in pathlist:
    imgpathlist.append(cv.imread(os.path.join(foldermodelpath,path)))
    

#load encoding file

file=open("encoding.p","rb")
encodelistknownid=pickle.load(file)
file.close()
encoding_list,stdID=encodelistknownid



while True:
    succ,img=capm.read()
    imgs=cv.resize(img,(0,0),None,0.25,0.25)
    imgs=cv.cvtColor(imgs,cv.COLOR_BGR2RGB)

    imgrect=img.copy()


    face_corframe=face_recognition.face_locations(imgs)
    encoding_currframe=face_recognition.face_encodings(imgs,face_corframe)

    for encoface, facelocat in zip(encoding_currframe,face_corframe):
        match=face_recognition.compare_faces(encoding_list,encoface)
        facedistace=face_recognition.face_distance(encoding_list,encoface)
        

        matchindex=np.argmin(facedistace)
        #print("mach index :",matchindex)
        print(facelocat)
        if match[matchindex]:
            print("known face dected")
            print("ID :",stdID[matchindex])
            font=cv.FONT_HERSHEY_SIMPLEX
            y1 ,x2 ,y2 , x1 =facelocat
            y1 ,x2 ,y2 , x1=y1*4 ,x2*4 ,y2*4 , x1*4
            bbox=  y1 ,x2 ,y2 , x1
            imgrect=cv.rectangle(imgrect,(x1,y1),(x2,y2),(0,255,0),3)
            imgrect=cv.putText(imgrect,f"Id:{stdID[matchindex]},'  face distace :',{facedistace} " ,(x1,y1+4),font,1,(0,255,0),1,cv.LINE_4)
            

        



    
    cv.imshow("img",imgrect)
    #cv.imshow("imgback",background)
    
    if cv.waitKey(1)== ord("q"):
        break