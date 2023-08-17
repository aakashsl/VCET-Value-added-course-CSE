from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('greet/', views.greet),
    path('greet/<str:name>', views.greet_person),
    path('myform/', views.myform)
]
