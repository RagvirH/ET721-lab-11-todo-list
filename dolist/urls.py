from django.urls import path
from . import views

urlpatterns = [
    #load page of the app will be send to the
    #index.html file
    path('',views.index, name='index')
]