# Generated by Django 5.1.4 on 2024-12-11 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstallmentType',
            fields=[
                ('idInstallmentType', models.AutoField(primary_key=True, serialize=False)),
                ('installment', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('idPropertyType', models.AutoField(primary_key=True, serialize=False)),
                ('PropertyType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateFinishing',
            fields=[
                ('idRealEstateFinishing', models.AutoField(primary_key=True, serialize=False)),
                ('typeFinishing', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionType',
            fields=[
                ('idTransactionType', models.AutoField(primary_key=True, serialize=False)),
                ('transactionType', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idUser', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Governorate', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('District', models.CharField(max_length=50)),
                ('street', models.CharField(max_length=50)),
                ('locationGPS', models.CharField(max_length=50)),
                ('ownerType', models.CharField(max_length=50)),
                ('electricityMeter', models.BooleanField(default=True)),
                ('waterMeter', models.BooleanField(default=True)),
                ('creationDateTime', models.DateTimeField(max_length=500, null=True)),
                ('idInstallmentType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='place.installmenttype')),
                ('idPropertyType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='place.propertytype')),
                ('idRealEstateFinishing', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='place.realestatefinishing')),
                ('idTransactionType', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='place.transactiontype')),
                ('idUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.users')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('idImage', models.AutoField(primary_key=True, serialize=False)),
                ('imageUrl', models.CharField(max_length=50)),
                ('idPlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.places')),
            ],
        ),
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('idAudio', models.AutoField(primary_key=True, serialize=False)),
                ('audioUrl', models.CharField(max_length=50)),
                ('idPlace', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='place.places')),
            ],
        ),
        migrations.CreateModel(
            name='Shops',
            fields=[
                ('shopsId', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.IntegerField()),
                ('description', models.CharField(max_length=500, null=True)),
                ('idPlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.places')),
                ('idRealEstateFinishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.realestatefinishing')),
                ('idTransactionType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.transactiontype')),
            ],
        ),
        migrations.CreateModel(
            name='Offices',
            fields=[
                ('officeId', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.IntegerField()),
                ('roomNumber', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('idPlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.places')),
                ('idRealEstateFinishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.realestatefinishing')),
                ('idTransactionType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.transactiontype')),
            ],
        ),
        migrations.CreateModel(
            name='EmptyLand',
            fields=[
                ('idEmptyLand', models.AutoField(primary_key=True, serialize=False)),
                ('propertyNumber', models.CharField(max_length=50, null=True)),
                ('Wight', models.IntegerField()),
                ('hight', models.IntegerField()),
                ('roomNumber', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('idPlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.places')),
                ('idRealEstateFinishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.realestatefinishing')),
                ('idTransactionType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.transactiontype')),
            ],
        ),
        migrations.CreateModel(
            name='Chalet',
            fields=[
                ('chaletId', models.AutoField(primary_key=True, serialize=False)),
                ('area', models.IntegerField()),
                ('description', models.CharField(max_length=500, null=True)),
                ('idPlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.places')),
                ('idRealEstateFinishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.realestatefinishing')),
                ('idTransactionType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.transactiontype')),
            ],
        ),
        migrations.CreateModel(
            name='Apartments',
            fields=[
                ('idApartments', models.AutoField(primary_key=True, serialize=False)),
                ('propertyNumber', models.CharField(max_length=50, null=True)),
                ('floorNumber', models.CharField(max_length=50, null=True)),
                ('apartmentNumber', models.CharField(max_length=50, null=True)),
                ('area', models.IntegerField()),
                ('roomNumber', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('idPlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.places')),
                ('idRealEstateFinishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.realestatefinishing')),
                ('idTransactionType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.transactiontype')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('idVideo', models.AutoField(primary_key=True, serialize=False)),
                ('videoUrl', models.CharField(max_length=50)),
                ('idPlace', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='place.places')),
            ],
        ),
        migrations.CreateModel(
            name='Villa',
            fields=[
                ('idVilla', models.AutoField(primary_key=True, serialize=False)),
                ('propertyNumber', models.CharField(max_length=50, null=True)),
                ('floorNumber', models.IntegerField(null=True)),
                ('area', models.IntegerField()),
                ('bedroomNumber', models.IntegerField(null=True)),
                ('bathroomNumber', models.IntegerField(null=True)),
                ('receptionNumber', models.IntegerField(null=True)),
                ('kitchenNumber', models.IntegerField(null=True)),
                ('description', models.CharField(max_length=500, null=True)),
                ('gardenArea', models.IntegerField()),
                ('idPlace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.places')),
                ('idRealEstateFinishing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.realestatefinishing')),
                ('idTransactionType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='place.transactiontype')),
            ],
        ),
    ]