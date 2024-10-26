from django.db import models

# Create your models here.
class tweet(models.Model):
    uname=models.CharField(max_length=30)
    post=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField('auth.User',related_name='blog_posts')
    
    def __str__(self):
        return self.uname
    
    def total_likes(self):
        return self.likes.count()