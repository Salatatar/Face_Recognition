from django.shortcuts import render
import pyrebase

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

# Create your views here.
def home(request):
    data = []
    all_users = db.child("Data").get()
    for content in all_users.each():
        message = content.val()
        data.append(message)
    return render(request, "home.html", {"data": data})