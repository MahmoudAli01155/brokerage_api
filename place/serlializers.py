from rest_framework import serializers
from .models import *


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

        def validate_idUsersSerializer(self, value):
            if Users.objects.filter(idUser=value).exists():
                raise serializers.ValidationError(f"User with ID '{value}' already exists.")
            return value


class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Places
        fields = '__all__'

class VillaSerializer(serializers.ModelSerializer):
    place = PlacesSerializer(source='idPlace')
    class Meta:
        model = Villa
        fields = '__all__'

class ApartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartments
        fields = '__all__'
        def validate_idApartmentsSerializer(self, value):
            if Apartments.objects.filter(idUser=value).exists():
                raise serializers.ValidationError(f"User with ID '{value}' already exists.")
            return value

class InstallmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstallmentType
        fields = '__all__'

        def validate_idInstallmentTypeSerializer(self, value):
            if Apartments.objects.filter(idUser=value).exists():
                raise serializers.ValidationError(f"User with ID '{value}' already exists.")
            return value

class RealEstateFinishingSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateFinishing
        fields = '__all__'

        def validate_idRealEstateFinishingSerializer(self, value):
            if RealEstateFinishing.objects.filter(idUser=value).exists():
                raise serializers.ValidationError(f"User with ID '{value}' already exists.")
            return value

class TransactionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionType
        fields = '__all__'

        def validate_idTransactionTypeSerializer(self, value):
            if TransactionType.objects.filter(idUser=value).exists():
                raise serializers.ValidationError(f"User with ID '{value}' already exists.")
            return value

class VillaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Villa
        fields = '__all__'

        def validate_idVillaSerialize(self, value):
            if Villa.objects.filter(idUser=value).exists():
                raise serializers.ValidationError(f"User with ID '{value}' already exists.")
            return value

class EmptyLandSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmptyLand
        fields = '__all__'

        def validate_idEmptyLandSerializer(self, value):
            if EmptyLand.objects.filter(idUser=value).exists():
                raise serializers.ValidationError(f"User with ID '{value}' already exists.")
            return value

class OfficesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offices
        fields = '__all__'

        def validate_idOfficesSerializer(self, value):
            if Offices.objects.filter(idUser=value).exists():
                raise serializers.ValidationError(f"User with ID '{value}' already exists.")
            return value

class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = '__all__'

        def validate_idShopsSerializer(self, value):
            if Shops.objects.filter(idUser=value).exists():
                raise serializers.ValidationError(f"User with ID '{value}' already exists.")
            return value

class ChaletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chalet
        fields = '__all__'

        def validate_idChaletSerializer(self, value):
            if Chalet.objects.filter(idUser=value).exists():
                raise serializers.ValidationError(f"User with ID '{value}' already exists.")
            return value
