from .views import *

from django.contrib import admin
from django.urls import path




urlpatterns = [
    path('adduser/',addUser,name='adduser'),
    path('getAllUsers', getAllUsersSerializer, name='getAllUsers'),
    path('top-five-villas', TopFiveVillasView.as_view(), name='getTopFiveVilla'),
    path('top-five-places', TopFivePlaceView.as_view(), name='getTopFivePlace'),
    path('create-apartment/', CreateApartmentsView.as_view(), name='create-apartment'),
    path('create-villa/', CreateVillaView.as_view(), name='create-villa'),
    path('create-emptyLand/', CreateEmptyLandView.as_view(), name='create-emptyLand'),
    path('create-offices/', CreateOfficesView.as_view(), name='create-offices'),
    path('create-Shops/', CreateShopsView.as_view(), name='create-Shops'),
    path('create-chalet/', CreateChaletView.as_view(), name='create-chalet'),
    path('update-apartment/', UpdateApartmentView.as_view(), name='update-apartment'),
    # path('create-place', CreatePlaceView.as_view(), name='createPlace'),
    ]