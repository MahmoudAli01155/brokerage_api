from .views import *

from django.contrib import admin
from django.urls import path




urlpatterns = [
    path('adduser/',addUser,name='adduser'),
    path('getAllUsers', getAllUsersSerializer, name='getAllUsers'),
    path('top-five-villas', TopFiveVillasView.as_view(), name='getTopFiveVilla'),
    path('top-five-places', TopFivePlaceView.as_view(), name='getTopFivePlace'),
    ]