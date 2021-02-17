from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ImageForm
import pyrebase
import shutil
import os
from .models import Image

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

def set_firebase():
    path_current = os.getcwd()
    data_test = []
    key_test = ""
    file_name = path_current + "/media/images/testimg.jpg"
    cloud_name = "images/img0.jpg"
    data = {'name': "TestImage", "class": "Class 0"}
    db.child("Name").push(data)
    storage.child(cloud_name).put(file_name)
    people = db.child("Name").get()
    for content in people.each():
        dbData = content.val()
        key_test = content.key()
        data_test.append(dbData)
    if len(data_test) > 1 :
        db.child("Name").child(key_test).remove()
    else :
        pass

def add(request):
    return render(request, 'add_image.html', {})

def add_image(request):
    subject = ""
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            obj = form.instance
            subject = request.POST["class"]
            set_firebase()
            update_firebase(subject)
            form = ImageForm()
            return render(request,"add_image.html", {"form": form, "obj" : obj, 'alert_flag': True})
    else:
        form = ImageForm()
    return render(request,"add_image.html", {"form": form})

def update_firebase(subject):
    data_list = []
    path_current = os.getcwd()
    lastimg = Image.objects.last()
    imgpath = lastimg.image.url
    imgname = lastimg.name
    data = {'name': imgname, "class": subject}
    people = db.child("Name").get()
    for content in people.each():
        dbData = content.val()
        data_list.append(dbData)
    count = len(data_list)
    file_name = path_current + imgpath
    cloud_name = "images/img"+str(count)+".jpg"
    db.child("Name").push(data)
    storage.child(cloud_name).put(file_name)