from django.db import models
from django.contrib import admin
class carshowroom(models.Model):
    plate_number = models.IntegerField(primary_key=True)
    color = models.CharField(max_length=12)
    amount = models.IntegerField()
    type = models.CharField(max_length=20)
    year = models.IntegerField()
class carshowroomAdmin(admin.ModelAdmin):
    list_display = ["plate_number","color","amount","type","year"]
     