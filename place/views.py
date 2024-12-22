# from django.shortcuts import render
import json
from tkinter import Place

from django.contrib.gis.geos.prototypes import create_point
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import *
from .serlializers import *
# Create your views here.

# HOME PAGE API FUNCTION
# ############################################################################
@api_view(['POST'])
def addUser(request):
    serializer = UsersSerializer(data=request.data)

    # Validate input data
    if serializer.is_valid():
        serializer.save()  # Create user
        return Response({"message": "User created successfully", "data": serializer.data},
                        status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TopFivePlaceView(APIView):
    def get(self, request):
        places = Places.objects.order_by('-id')[:5]
        serializer = PlacesSerializer(places, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # try:
        #
        # except Exception as e:
        #     return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
def getAllUsersSerializer(request):
    items = Users.objects.all()
    if items:
        serializer = UsersSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class TopFiveApartmentsView(APIView):
    def get(self, request):
        try:
            apartments = Apartments.objects.select_related('idPlace').order_by('-idVilla')[:5]
            serializer = ApartmentsSerializer(apartments, many=True)

            for apartment in serializer.data:
                place = apartment['idPlace']
                placeDetails =Places.objects.filter(id=place)
                placeSerializer = PlacesSerializer(placeDetails, many=True)
                apartment['idPlace'] = placeSerializer.data


            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TopFiveVillasView(APIView):
    def get(self, request):
        try:
            villas = Villa.objects.select_related('idPlace').order_by('-idVilla')[:5]
            serializer = VillaSerializer(villas, many=True)

            for villa in serializer.data:
                place = villa['idPlace']
                placeDetails =Places.objects.filter(id=place)
                placeSerializer = PlacesSerializer(placeDetails, many=True)
                villa['idPlace'] = placeSerializer.data


            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class TopFiveEmptyLandView(APIView):
    def get(self, request):
        try:
            emptyLands = EmptyLand.objects.select_related('idPlace').order_by('-idVilla')[:5]
            serializer = EmptyLandSerializer(emptyLands, many=True)

            for emptyLand in serializer.data:
                place = emptyLand['idPlace']
                placeDetails =Places.objects.filter(id=place)
                placeSerializer = PlacesSerializer(placeDetails, many=True)
                emptyLand['idPlace'] = placeSerializer.data


            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class TopFiveOfficesView(APIView):
    def get(self, request):
        try:
            offices = Offices.objects.select_related('idPlace').order_by('-idVilla')[:5]
            serializer = OfficesSerializer(offices, many=True)

            for office in serializer.data:
                place = office['idPlace']
                placeDetails =Places.objects.filter(id=place)
                placeSerializer = PlacesSerializer(placeDetails, many=True)
                office['idPlace'] = placeSerializer.data


            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class TopFiveShopsView(APIView):
    def get(self, request):
        try:
            shops = Shops.objects.select_related('idPlace').order_by('-idVilla')[:5]
            serializer = ShopsSerializer(shops, many=True)

            for shop in serializer.data:
                place = shop['idPlace']
                placeDetails =Places.objects.filter(id=place)
                placeSerializer = PlacesSerializer(placeDetails, many=True)
                shop['idPlace'] = placeSerializer.data


            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class TopFiveChaletView(APIView):
    def get(self, request):
        try:
            chalets = Chalet.objects.select_related('idPlace').order_by('-idVilla')[:5]
            serializer = ChaletSerializer(chalets, many=True)

            for chalet in serializer.data:
                place = chalet['idPlace']
                placeDetails =Places.objects.filter(id=place)
                placeSerializer = PlacesSerializer(placeDetails, many=True)
                chalet['idPlace'] = placeSerializer.data


            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


####################### SEARCH ###################################################
#####################################################################################################################

class SearchVillaView(APIView):
    def get(self, request):
        query = request.query_params.get('query', None)
        if not query:
            return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
        villas = Villa.objects.filter( models.Q(description__icontains=query) |
                                       models.Q(idPlace__city__icontains=query) |
                                       models.Q(idPlace__governorate__icontains=query)
                                       ).select_related('idPlace')
        serializer = VillaSerializer(villas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)






######################################################################################################
############## create adds id [create adds] pages #######################################################


class CreateApartmentsView(APIView):
    def post(self, request):
        try:
            if Users.objects.filter(idUser=request.data['idUser']).exists():
                createPlace = Places.objects.create(idUser=request.data['idUser'])
                UsersSerializer.Meta.validate_idUsersSerializer
                if createPlace:
                    Apartments.objects.create(
                        idPlace=createPlace,
                        propertyNumber=request.data['propertyNumber'],
                        floorNumber=request.data['floorNumber'],
                        apartmentNumber=request.data['apartmentNumber'],
                        area=request.data['area'],
                        roomNumber=request.data['roomNumber'],
                        description=request.data['description'],
                        Governorate=request.data['Governorate'],
                        city=request.data['city'],
                        District=request.data['District'],
                        street=request.data['street'],
                        locationGPS=request.data['locationGPS'],
                        ownerType=request.data['ownerType'],
                        electricityMeter=request.data['electricityMeter'],
                        waterMeter=request.data['waterMeter'],
                        idPropertyType=request.data['idPropertyType'],
                        idRealEstateFinishing=request.data['idRealEstateFinishing'],
                        idTransactionType=request.data['idTransactionType'],
                        idInstallmentType=request.data['idInstallmentType'],
                    )

                    # images = json.loads(request.body['images'])
                    for image in json.loads(request.body['images']):
                        Image.objects.create(
                            imageUrl=image['imageUrl'],
                            idPlace=createPlace,
                        )
                    Video.objects.create(
                        videoUrl=request.data['videoUrl'],
                        idPlace=createPlace,
                    )
                    Image.objects.create(
                        audioUrl=request.data['audioUrl'],
                        idPlace=createPlace,
                    )


                    return Response({"message": "Apartment created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateVillaView(APIView):
    def post(self, request):
        try:
            if Users.objects.filter(idUser=request.data['idUser']).exists():
                createPlace = Places.objects.create(idUser=request.data['idUser'])
                if createPlace:
                    Villa.objects.create(
                        idPlace=createPlace,
                        propertyNumber=request.data['propertyNumber'],
                        floorNumber = request.data['floorNumber'],
                        area = request.data['area'],
                        bedroomNumber = request.data['bedroomNumber'],
                        bathroomNumber = request.data['bathroomNumber'],
                        receptionNumber = request.data['receptionNumber'],
                        kitchenNumber = request.data['kitchenNumber'],
                        description = request.data['description'],
                        gardenArea = request.data['gardenArea'],
                        Governorate = request.data['Governorate'],
                        city = request.data['city'],
                        District = request.data['District'],
                        street = request.data['street'],
                        locationGPS = request.data['locationGPS'],
                        ownerType = request.data['ownerType'],
                        electricityMeter = request.data['electricityMeter'],
                        waterMeter = request.data['waterMeter'],
                        idPropertyType = request.data['idPropertyType'],
                        idRealEstateFinishing = request.data['idRealEstateFinishing'],
                        idTransactionType = request.data['idTransactionType'],
                        idInstallmentType = request.data['idInstallmentType'],
                    )

                    # images = json.loads(request.body['images'])
                    for image in json.loads(request.body['images']):
                        Image.objects.create(
                            imageUrl=image['imageUrl'],
                            idPlace=createPlace,
                        )
                    Video.objects.create(
                        videoUrl=request.data['videoUrl'],
                        idPlace=createPlace,
                    )
                    Image.objects.create(
                        audioUrl=request.data['audioUrl'],
                        idPlace=createPlace,
                    )


                    return Response({"message": "Villa created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateEmptyLandView(APIView):
    def post(self, request):
        try:
            if Users.objects.filter(idUser=request.data['idUser']).exists():
                createPlace = Places.objects.create(idUser=request.data['idUser'])
                if createPlace:
                    EmptyLand.objects.create(
                        idPlace=createPlace,
                        propertyNumber=request.data['propertyNumber'],
                        Wight = request.data['Wight'],
                        hight = request.data['hight'],
                        roomNumber = request.data['roomNumber'],
                        description = request.data['description'],
                        Governorate = request.data['Governorate'],
                        city = request.data['city'],
                        District = request.data['District'],
                        street = request.data['street'],
                        locationGPS = request.data['locationGPS'],
                        ownerType = request.data['ownerType'],
                        electricityMeter = request.data['electricityMeter'],
                        waterMeter = request.data['waterMeter'],
                        creationDateTime = request.data['creationDateTime'],
                        idPropertyType = request.data['idPropertyType'],
                        idRealEstateFinishing = request.data['idRealEstateFinishing'],
                        idTransactionType = request.data['idTransactionType'],
                        idInstallmentType = request.data['idInstallmentType'],

                    )

                    # images = json.loads(request.body['images'])
                    for image in json.loads(request.body['images']):
                        Image.objects.create(
                            imageUrl=image['imageUrl'],
                            idPlace=createPlace,
                        )
                    Video.objects.create(
                        videoUrl=request.data['videoUrl'],
                        idPlace=createPlace,
                    )
                    Image.objects.create(
                        audioUrl=request.data['audioUrl'],
                        idPlace=createPlace,
                    )


                    return Response({"message": "EmptyLand created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CreateOfficesView(APIView):
    def post(self, request):
        try:
            if Users.objects.filter(idUser=request.data['idUser']).exists():
                createPlace = Places.objects.create(idUser=request.data['idUser'])
                if createPlace:
                    Offices.objects.create(
                        idPlace=createPlace,
                        propertyNumber=request.data['propertyNumber'],
                        area=request.data['propertyNumber'],
                        roomNumber = request.data['propertyNumber'],
                        description = request.data['propertyNumber'],
                        Governorate = request.data['propertyNumber'],
                        city = request.data['propertyNumber'],
                        District = request.data['propertyNumber'],
                        street = request.data['propertyNumber'],
                        locationGPS = request.data['propertyNumber'],
                        ownerType = request.data['propertyNumber'],
                        electricityMeter = request.data['propertyNumber'],
                        waterMeter = request.data['propertyNumber'],
                        creationDateTime = request.data['propertyNumber'],
                        idPropertyType = request.data['propertyNumber'],
                        idRealEstateFinishing = request.data['propertyNumber'],
                        idTransactionType = request.data['propertyNumber'],
                        idInstallmentType =request.data['propertyNumber'],
                    )

                    # images = json.loads(request.body['images'])
                    for image in json.loads(request.body['images']):
                        Image.objects.create(
                            imageUrl=image['imageUrl'],
                            idPlace=createPlace,
                        )
                    Video.objects.create(
                        videoUrl=request.data['videoUrl'],
                        idPlace=createPlace,
                    )
                    Image.objects.create(
                        audioUrl=request.data['audioUrl'],
                        idPlace=createPlace,
                    )


                    return Response({"message": "Offices created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class CreateShopsView(APIView):
    def post(self, request):
        try:
            if Users.objects.filter(idUser=request.data['idUser']).exists():
                createPlace = Places.objects.create(idUser=request.data['idUser'])
                if createPlace:
                    Shops.objects.create(
                        idPlace=createPlace,
                        propertyNumber=request.data['propertyNumber'],
                        area=request.data['area'],
                        description = request.data['description'],
                        Governorate = request.data['Governorate'],
                        city = request.data['city'],
                        District = request.data['District'],
                        street = request.data['street'],
                        locationGPS = request.data['locationGPS'],
                        ownerType = request.data['ownerType'],
                        electricityMeter = request.data['electricityMeter'],
                        waterMeter = request.data['waterMeter'],
                        idPropertyType = request.data['idPropertyType'],
                        idRealEstateFinishing = request.data['idRealEstateFinishing'],
                        idTransactionType = request.data['idTransactionType'],
                        idInstallmentType =request.data['idInstallmentType'],
                    )

                    # images = json.loads(request.body['images'])
                    for image in json.loads(request.body['images']):
                        Image.objects.create(
                            imageUrl=image['imageUrl'],
                            idPlace=createPlace,
                        )
                    Video.objects.create(
                        videoUrl=request.data['videoUrl'],
                        idPlace=createPlace,
                    )
                    Image.objects.create(
                        audioUrl=request.data['audioUrl'],
                        idPlace=createPlace,
                    )


                    return Response({"message": "Shops created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CreateChaletView(APIView):
    def post(self, request):
        try:
            if Users.objects.filter(idUser=request.data['idUser']).exists():
                createPlace = Places.objects.create(idUser=request.data['idUser'])
                if createPlace:
                    Chalet.objects.create(
                        idPlace=createPlace,
                        propertyNumber=request.data['propertyNumber'],
                        area=request.data['area'],
                        description = request.data['description'],
                        Governorate = request.data['Governorate'],
                        city = request.data['city'],
                        District = request.data['District'],
                        street = request.data['street'],
                        locationGPS = request.data['locationGPS'],
                        ownerType = request.data['ownerType'],
                        electricityMeter = request.data['electricityMeter'],
                        waterMeter = request.data['waterMeter'],
                        idPropertyType = request.data['idPropertyType'],
                        idRealEstateFinishing = request.data['idRealEstateFinishing'],
                        idTransactionType = request.data['idTransactionType'],
                        idInstallmentType =request.data['idInstallmentType'],
                    )

                    # images = json.loads(request.body['images'])
                    for image in json.loads(request.body['images']):
                        Image.objects.create(
                            imageUrl=image['imageUrl'],
                            idPlace=createPlace,
                        )
                    Video.objects.create(
                        videoUrl=request.data['videoUrl'],
                        idPlace=createPlace,
                    )
                    Image.objects.create(
                        audioUrl=request.data['audioUrl'],
                        idPlace=createPlace,
                    )


                    return Response({"message": "Chalet created successfully"}, status=status.HTTP_201_CREATED)
            else:
                return Response({"error": "User does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#####################################################################################################################





class UpdateApartmentView(APIView):
    def put(self, request):
        try:
            apartment = Apartments.objects.get(id=request.data["id"])
            serializer = ApartmentsSerializer(apartment, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Apartments.DoesNotExist:
            return Response({"error": "Apartment not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# class UpdateVillaView(APIView):
#     def put(self, request, pk):
#         try:
#             villa = Villa.objects.get(id=request.data["id"])
#             serializer = VillaSerializer(villa, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         except Villa.DoesNotExist:
#             return Response({"error": "Villa not found"}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#




#==================   Here Is Functions  (Show Id)  ==============================

@api_view(['GET'])
def Get_Villa_By_Id(request,pk):
    try:
        data = Villa.objects.get(idVilla=pk)
        if request.method == "GET":
            serilaizer = VillaSerializer(data)
            return Response(serilaizer.data)
    except:
        return Response({"message":"This property does not exist"})


@api_view(['Get'])
def Get_Apartment_By_Id(request,pk):
    try:
        data = Apartments.objects.get(idApartments=pk)
        if request.method == "GET":
            serilaizer = ApartmentsSerializer(data)
            return Response(serilaizer.data)
    except:
        return Response({"message":"This property does not exist"})

@api_view(['Get'])
def Get_EmptyLand_By_Id(request,pk):
    try:
        data = EmptyLand.objects.get(idEmptyLand=pk)
        if request.method == "GET":
            serilaizer = EmptyLandSerializer(data)
            return Response(serilaizer.data)
    except:
        return Response({"message":"This property does not exist"})

@api_view(['Get'])
def Get_Office_By_Id(request,pk):
    try:

        data = Offices.objects.get(idEmptyLand=pk)
        if request.method == "GET":
            serilaizer = OfficesSerializer(data)
            return Response(serilaizer.data)
    except:
        return Response({"message":"This property does not exist"})


@api_view(['Get'])
def Get_Shop_By_Id(request,pk):
    try:
        data = Shops.objects.get(idEmptyLand=pk)
        if request.method == "GET":
            serilaizer = ShopsSerializer(data)
            return Response(serilaizer.data)
    except:
        return Response({"message":"This property does not exist"})
    

@api_view(['Get'])
def Get_Chalet_By_Id(request,pk):
    try:

        data = Chalet.objects.get(idEmptyLand=pk)
        if request.method == "GET":
            serilaizer = ChaletSerializer(data)
            return Response(serilaizer.data)
    except:
        return Response({"message":"This property does not exist"})
    

#========================================================

