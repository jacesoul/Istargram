from django.db import models

# Create your models here.

class Signup(models.Model): 
    email = models.EmailField(
        max_length = 100,
        unique     = True,
    )    
    password = models.CharField(
        max_length = 100,
        unique     = True,
    )    
    phone_number = models.CharField(max_length = 20)
    nickname     = models.CharField(max_length = 20)