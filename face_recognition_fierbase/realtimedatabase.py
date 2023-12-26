
import firebase_admin
from firebase_admin import credentials,db

cred = credentials.Certificate("project_product\serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancesystem-76762-default-rtdb.firebaseio.com/"

                            }  )
ref=db.reference('Students')

data={
    
    '001':
    {
    "name":"elon",
    
    "major":"computer",
    "Lecture sub":"PPS",
    "Attendance time":" 00:54:34",
    "Total attendance":10,
    },
    '002':
    {
    "name":"elon",
    "major":"computer",
    "Lecture sub":"PPS",
    "Attendance date time":"00:54:34",
    "Total attendance":10,
    },
    '003':
    {
    "name":"elon",
    "major":"computer",
    "Lecture sub":"PPS",
    "Attendance date time":" 00:54:34",
    "Total attendance":10,
    },
    '004':
    {
    "name":"elon",
    "major":"computer",
    "Lecture sub":"PPS",
    "Attendance date time":" 00:54:34",
    "Total attendance":10,
    },
    '005':
    {
    "name":"elon",
    "major":"computer",
    "Lecture sub":"PPS",
    "Attendance date time":" 00:54:34",
    "Total attendance":10,
    },
    '006':
    {
    "name":"elon",
    "major":"computer",
    "Lecture sub":"PPS",
    "Attendance date time":"00:54:34",
    "Total attendance":10,
    }
}

for key,value in data.items():
    ref.child(key).set(value)