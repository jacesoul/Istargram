from django.db import models
from users.models import Signup

# Create your models here.

class User(models.Model):
    # email = models.ForeignKey("Signup", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    like_post = models.ManyToManyField('Post',through='Like',related_name='like_user')
    comment_post = models.ManyToManyField('Post',through='Comment',related_name='comment_user', null=True)
    class Meta:
        db_table = 'users'

class Post(models.Model): 
    name = models.ForeignKey('User', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add =True)
    updated_at=models.DateTimeField(auto_now =True)
    image_url=models.URLField(max_length=200)
    title=models.CharField(max_length=100, default='awesome')
    content=models.CharField(max_length=1000, default='Hello World!')
    class Meta:
        db_table = 'posts'

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    comment_post = models.ForeignKey('User',on_delete=models.CASCADE, related_name='comment_user',null=True)
    created_at=models.DateTimeField(auto_now_add =True)
    updated_at=models.DateTimeField(auto_now =True)
    content = models.CharField(max_length=1000)
    comment_id = models.ForeignKey('Comment',on_delete=models.CASCADE, null=True)
    class Meta:
        db_table = 'comments'

class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    like_post = models.ForeignKey('User', on_delete=models.CASCADE, related_name = 'like_user',null=True)
    like = models.BooleanField(null=True)
    class Meta:
        db_table = 'likes'

class Follow(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE, related_name='follower',null=True)
    follow_user = models.ForeignKey('User',on_delete=models.CASCADE, related_name='followed',null=True)
    follow = models.BooleanField(null=True)
    class Meta: 
        db_table = 'follows'

