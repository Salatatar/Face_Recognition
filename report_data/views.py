from django.shortcuts import render
from django.http import HttpResponse
from shutil import copyfile
import os.path
from os import path
import pyrebase
import os

firebaseConfig = {
    'apiKey': "AIzaSyBHn-PVdt-neRToPoZIEVcsR-eMc0565NU",
    'authDomain': "web-face-recognition.firebaseapp.com",
    'databaseURL': "https://web-face-recognition.firebaseio.com",
    'projectId': "web-face-recognition",
    'storageBucket': "web-face-recognition.appspot.com",
    'messagingSenderId': "164666117507",
    'appId': "1:164666117507:web:45e9181b99f99383e5bab6"
  }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

storage = firebase.storage()

test = "TestImage"

name_upload = []

def report_data(request):
    download_image()
    total_data = []
    for i in range(len(name_upload)):
        data_learn_sa = []
        data_late_sa = []
        data_learn_ml = []
        data_late_ml = []
        data_learn_iot = []
        data_late_iot = []
        people = db.child("Data").order_by_child("Name").equal_to(name_upload[i]).get()
        for person in people.each():
            if person.val()["Status"] == "learn" and person.val()["Subject"] == "Class SA":
                message = person.val()
                data_learn_sa.append(message)
            elif person.val()["Status"] == "late" and person.val()["Subject"] == "Class SA":
                message = person.val()
                data_late_sa.append(message)
            elif person.val()["Status"] == "learn" and person.val()["Subject"] == "Class ML":
                message = person.val()
                data_learn_ml.append(message)
            elif person.val()["Status"] == "late" and person.val()["Subject"] == "Class ML":
                message = person.val()
                data_late_ml.append(message)
            elif person.val()["Status"] == "learn" and person.val()["Subject"] == "Class iot":
                message = person.val()
                data_learn_iot.append(message)
            elif person.val()["Status"] == "late" and person.val()["Subject"] == "Class iot":
                message = person.val()
                data_late_iot.append(message)
        # check_data(data_learn_sa, data_learn_ml, data_late_sa, data_late_ml, data_learn_iot, data_late_iot)
        if len(data_late_sa) != 0:
            # print(len(data_late_sa))
            data_late_sa[0]["Late"] = len(data_late_sa)
            if len(data_learn_sa) != 0:
                # print(len(data_learn_sa))
                data_late_sa[0]["Learn"] = len(data_learn_sa)
            else:
                data_late_sa[0]["Learn"] = len(data_learn_sa)
            total_data.append(data_late_sa[0])
        elif len(data_learn_sa) != 0:
            # print(len(data_learn_sa))
            data_learn_sa[0]["Learn"] = len(data_learn_sa)
            if len(data_late_sa) != 0:
                # print(len(data_late_sa))
                data_learn_sa[0]["Late"] = len(data_late_sa)
            else:
                data_learn_sa[0]["Late"] = len(data_late_sa)
            total_data.append(data_learn_sa[0])
        else:
            # print("NO")
            pass
        if len(data_late_ml) != 0:
            # print(len(data_late_ml))
            data_late_ml[0]["Late"] = len(data_late_ml)
            if len(data_learn_ml) != 0:
                # print(len(data_learn_ml))
                data_late_ml[0]["Learn"] = len(data_learn_ml)
            else:
                data_late_ml[0]["Learn"] = len(data_learn_ml)
            total_data.append(data_late_ml[0])
        elif len(data_learn_ml) != 0:
            # print(len(data_learn_ml))
            data_learn_ml[0]["Learn"] = len(data_learn_ml)
            if len(data_late_ml) != 0:
                # print(len(data_late_ml))
                data_learn_ml[0]["Late"] = len(data_late_ml)
            else:
                data_learn_ml[0]["Late"] = len(data_late_ml)
            total_data.append(data_learn_ml[0])
        else:
            # print("NO")
            pass
        if len(data_late_iot) != 0:
            # print(len(data_late_iot))
            data_late_iot[0]["Late"] = len(data_late_iot)
            if len(data_learn_iot) != 0:
                # print(len(data_learn_iot))
                data_late_iot[0]["Learn"] = len(data_learn_iot)
            else:
                data_late_iot[0]["Learn"] = len(data_learn_iot)
            total_data.append(data_late_iot[0])
        elif len(data_learn_iot) != 0:
            # print(len(data_learn_iot))
            data_learn_iot[0]["Learn"] = len(data_learn_iot)
            if len(data_late_iot) != 0:
                # print(len(data_late_iot))
                data_learn_iot[0]["Late"] = len(data_late_iot)
            else:
                data_learn_iot[0]["Late"] = len(data_late_iot)
            total_data.append(data_learn_iot[0])
        else:
            # print("NO")
            pass
    # print(total_data)
    return render(request, "reports.html", {"data": total_data})

def download_image():
    path_current = os.getcwd()
    people = db.child("Name").get()
    for person in people.each():
        name = person.val()["name"]
        if name not in name_upload and name != test:
            name_upload.append(name)
        else:
            pass
    for i in range(len(name_upload)):
        storage.child("images/img"+str(i + 1)+".jpg").download("", name_upload[i]+".jpg")

        src = path_current + "/" + name_upload[i]+".jpg"
        dst = path_current + "/static/image/" + name_upload[i]+".jpg"

        copyfile(src, dst)

        if path.exists(src) == True:
            os.remove(src)
        else:
            pass
