# from django.shortcuts import render
from tkinter import Place

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


# SEARCH
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







