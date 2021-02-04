from django.urls import path
from add_image import views

urlpatterns = [
    path('', views.add_image, name='add_image'),
]