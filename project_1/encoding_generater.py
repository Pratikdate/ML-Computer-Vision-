import cv2 as cv 
import face_recognition
import pickle
import os

foldermodelpath="project_1\img"
pathlist=os.listdir(foldermodelpath)
imgpathlist=[]

stdID=[]

for path in pathlist:
    imgpathlist.append(cv.imread(os.path.join(foldermodelpath,path)))
    stdID.append(os.path.splitext(path)[0])
print(stdID)


def findencoding(imagelist):
    encode_list=[]
    for img in imagelist:
        img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
        encode=face_recognition.face_encodings(img)[0]
        encode_list.append(encode)

    return encode_list

print("complete")
encoding_list=findencoding(imgpathlist)

encoding_list_id=[encoding_list,stdID]

file =open("encoding.p",'wb')
pickle.dump(encoding_list_id,file)
file.close()
