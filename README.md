# Ex02 Django ORM Web Application
## Date: 24/09/2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).





## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py
from django.contrib import admin
from.models import carshowroom,carshowroomAdmin
admin.site.register(carshowroom,carshowroomAdmin)

model.py
from django.db import models
from django.contrib import admin
class carshowroom(models.Model):
    plate_number = models.IntegerField(primary_key=True)
    color = models.CharField(max_length=12)
    amount = models.IntegerField()
    type = models.CharField(max_length=20)
    year = models.IntegerField()
class carshowroomAdmin(admin.ModelAdmin):
    list_display = ["plate_number","color","amount","type","year"]admin.py
from django.contrib import admin
from.models import carshowroom,carshowroomAdmin
admin.site.register(carshowroom,carshowroomAdmin)
     
```

## OUTPUT
![alt text](<Screenshot 2025-09-27 190908.png>)



## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
