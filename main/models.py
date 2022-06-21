from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    id=models.AutoField(primary_key=True)
    writer=models.ForeignKey(User,on_delete=models.CASCADE) #일대다관계
    title=models.CharField(max_length=200)
    writer=models.CharField(max_length=100)
    pub_date=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to="post/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]

class Comment(models.Model):
    content = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey( Post ,on_delete=models.CASCADE, related_name ='comments')
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now=True)
