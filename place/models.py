from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.AutoField(primary_key=True)
    idUser = models.CharField(max_length=100, unique=True)

class PropertyType(models.Model):
    idPropertyType = models.AutoField(primary_key=True)
    PropertyType = models.CharField(max_length=50)

class RealEstateFinishing(models.Model):
    idRealEstateFinishing = models.AutoField(primary_key=True)
    typeFinishing = models.CharField(max_length=50)

class TransactionType(models.Model):
    idTransactionType = models.AutoField(primary_key=True)
    transactionType = models.CharField(max_length=50)

class InstallmentType(models.Model):
    idInstallmentType = models.AutoField(primary_key=True)
    installment = models.CharField(max_length=50)

class Places(models.Model):
    id = models.AutoField(primary_key=True)
    idUser = models.ForeignKey(Users, on_delete=models.CASCADE)

class Image(models.Model):
    idImage = models.AutoField(primary_key=True)
    imageUrl = models.CharField(max_length=50)
    idPlace = models.ForeignKey(Places ,on_delete=models.CASCADE)

class Video(models.Model):
    idVideo = models.AutoField(primary_key=True)
    videoUrl = models.CharField(max_length=50)
    idPlace = models.OneToOneField(Places,on_delete=models.CASCADE)

class Audio(models.Model):
    idAudio = models.AutoField(primary_key=True)
    audioUrl = models.CharField(max_length=50)
    idPlace = models.OneToOneField(Places,on_delete=models.CASCADE)

class Apartments(models.Model):
    idPlace = models.ForeignKey(Places ,on_delete=models.CASCADE)
    idApartments = models.AutoField(primary_key=True)
    propertyNumber= models.CharField(max_length=50, null=True)
    floorNumber = models.CharField(max_length=50, null=True)
    apartmentNumber = models.CharField(max_length=50, null=True)
    area = models.IntegerField()
    roomNumber = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    Governorate = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    locationGPS = models.CharField(max_length=50)
    ownerType = models.CharField(max_length=50)
    electricityMeter = models.BooleanField(default=True)
    waterMeter = models.BooleanField(default=True)
    creationDateTime = models.DateTimeField(max_length=500, null=True)
    idPropertyType = models.ForeignKey(PropertyType, on_delete=models.CASCADE, null=True)
    idRealEstateFinishing = models.ForeignKey(RealEstateFinishing, on_delete=models.CASCADE, null=True)
    idTransactionType = models.ForeignKey(TransactionType, on_delete=models.CASCADE, null=True)
    idInstallmentType = models.ForeignKey(InstallmentType, on_delete=models.CASCADE, null=True)


class Villa(models.Model):
    idPlace = models.ForeignKey(Places, on_delete=models.CASCADE)
    idVilla = models.AutoField(primary_key=True)
    propertyNumber= models.CharField(max_length=50, null=True)
    floorNumber = models.IntegerField( null=True)
    area = models.IntegerField()
    bedroomNumber = models.IntegerField( null=True)
    bathroomNumber = models.IntegerField( null=True)
    receptionNumber = models.IntegerField( null=True)
    kitchenNumber = models.IntegerField( null=True)
    description = models.CharField(max_length=500, null=True)
    gardenArea = models.IntegerField()
    Governorate = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    locationGPS = models.CharField(max_length=50)
    ownerType = models.CharField(max_length=50)
    electricityMeter = models.BooleanField(default=True)
    waterMeter = models.BooleanField(default=True)
    creationDateTime = models.DateTimeField(max_length=500, null=True)
    idPropertyType = models.ForeignKey(PropertyType, on_delete=models.CASCADE, null=True)
    idRealEstateFinishing = models.ForeignKey(RealEstateFinishing, on_delete=models.CASCADE, null=True)
    idTransactionType = models.ForeignKey(TransactionType, on_delete=models.CASCADE, null=True)
    idInstallmentType = models.ForeignKey(InstallmentType, on_delete=models.CASCADE, null=True)


class EmptyLand(models.Model):
    idPlace = models.ForeignKey(Places, on_delete=models.CASCADE)
    idEmptyLand = models.AutoField(primary_key=True)
    propertyNumber= models.CharField(max_length=50, null=True)
    Wight = models.IntegerField()
    hight = models.IntegerField()
    roomNumber = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    Governorate = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    locationGPS = models.CharField(max_length=50)
    ownerType = models.CharField(max_length=50)
    electricityMeter = models.BooleanField(default=True)
    waterMeter = models.BooleanField(default=True)
    creationDateTime = models.DateTimeField(max_length=500, null=True)
    idPropertyType = models.ForeignKey(PropertyType, on_delete=models.CASCADE, null=True)
    idRealEstateFinishing = models.ForeignKey(RealEstateFinishing, on_delete=models.CASCADE, null=True)
    idTransactionType = models.ForeignKey(TransactionType, on_delete=models.CASCADE, null=True)
    idInstallmentType = models.ForeignKey(InstallmentType, on_delete=models.CASCADE, null=True)


class Offices(models.Model):
    idPlace = models.ForeignKey(Places ,on_delete=models.CASCADE)
    officeId = models.AutoField(primary_key=True)
    area = models.IntegerField()
    roomNumber = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, null=True)
    Governorate = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    locationGPS = models.CharField(max_length=50)
    ownerType = models.CharField(max_length=50)
    electricityMeter = models.BooleanField(default=True)
    waterMeter = models.BooleanField(default=True)
    creationDateTime = models.DateTimeField(max_length=500, null=True)
    idPropertyType = models.ForeignKey(PropertyType, on_delete=models.CASCADE, null=True)
    idRealEstateFinishing = models.ForeignKey(RealEstateFinishing, on_delete=models.CASCADE, null=True)
    idTransactionType = models.ForeignKey(TransactionType, on_delete=models.CASCADE, null=True)
    idInstallmentType = models.ForeignKey(InstallmentType, on_delete=models.CASCADE, null=True)


class Shops(models.Model):
    idPlace = models.ForeignKey(Places, on_delete=models.CASCADE)
    shopsId = models.AutoField(primary_key=True)
    area = models.IntegerField()
    description = models.CharField(max_length=500, null=True)
    Governorate = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    locationGPS = models.CharField(max_length=50)
    ownerType = models.CharField(max_length=50)
    electricityMeter = models.BooleanField(default=True)
    waterMeter = models.BooleanField(default=True)
    creationDateTime = models.DateTimeField(max_length=500, null=True)
    idPropertyType = models.ForeignKey(PropertyType, on_delete=models.CASCADE, null=True)
    idRealEstateFinishing = models.ForeignKey(RealEstateFinishing, on_delete=models.CASCADE, null=True)
    idTransactionType = models.ForeignKey(TransactionType, on_delete=models.CASCADE, null=True)
    idInstallmentType = models.ForeignKey(InstallmentType, on_delete=models.CASCADE, null=True)


class Chalet(models.Model):
    idPlace = models.ForeignKey(Places ,on_delete=models.CASCADE)
    chaletId = models.AutoField(primary_key=True)
    area = models.IntegerField()
    description = models.CharField(max_length=500, null=True)
    Governorate = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    locationGPS = models.CharField(max_length=50)
    ownerType = models.CharField(max_length=50)
    electricityMeter = models.BooleanField(default=True)
    waterMeter = models.BooleanField(default=True)
    creationDateTime = models.DateTimeField(max_length=500, null=True)
    idPropertyType = models.ForeignKey(PropertyType, on_delete=models.CASCADE, null=True)
    idRealEstateFinishing = models.ForeignKey(RealEstateFinishing, on_delete=models.CASCADE, null=True)
    idTransactionType = models.ForeignKey(TransactionType, on_delete=models.CASCADE, null=True)
    idInstallmentType = models.ForeignKey(InstallmentType, on_delete=models.CASCADE, null=True)


