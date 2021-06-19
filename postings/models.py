from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'users'

class Posting(models.Model): 

    name = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add =True)
    image_url=models.URLField(max_length=200)

    class Meta:
        db_table = 'postings'

