from django.db import models
from django.contrib import admin
class Cars (models.Model):
    car_id=models.IntegerField (primary_key=True)
    car_models=models
    car_models.CharField (max_length=20)
    email=models.EmailField()
    dop=models.DateField()
    car_Type=models.CharField(max_length=10)
class CarsAdmin(admin.ModelAdmin):
    list_display=["car_id","car_models","email","dop","car_Type"]
     
