from django.db import models

# Create your models here.

class Signup(models.Model): 
    email = models.EmailField(
        max_length = 100,
    )    
    password = models.CharField(
        max_length = 100,
    )    
    phone_number = models.CharField(max_length = 20, null=True)
    nickname     = models.CharField(max_length = 20, null=True)

    class Meta: 
        db_table = 'signups'