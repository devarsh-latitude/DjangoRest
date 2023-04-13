from django.urls import path
from . import views

urlpatterns=[
    path('',views.getData,name='getdata'),
    path('add/',views.addData,name='adddata'),
]