from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        db_table = 'users'

class Posting(models.Model): 
    name = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add =True)
    updated_at=models.DateTimeField(auto_now =True)
    image_url=models.URLField(max_length=200)
    title=models.CharField(max_length=500, default='awesome')
    class Meta:
        db_table = 'postings'


class Comment(models.Model):
    title=models.ForeignKey('Posting', on_delete=models.CASCADE)
    comment_user=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add =True)
    updated_at=models.DateTimeField(auto_now =True)
    content = models.CharField(max_length=1000)
    class Meta:
        db_table = 'comments'