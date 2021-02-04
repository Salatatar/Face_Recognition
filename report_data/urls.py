from django.urls import path
from report_data import views

urlpatterns = [
    path('', views.report_data, name='report'),
]