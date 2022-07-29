from pyexpat import model
from django.utils import timezone
from django.db import models
from django.forms import ModelForm

# Create your models here.

class users(models.Model):
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    UserMail = models.EmailField(max_length=100,unique=True)
    Password = models.CharField(max_length=15)
    image = models.FileField()
    otp = models.IntegerField(max_length=6,blank=True,null=True)
    def __str__(self):
        return self.FirstName   

class blogs(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    image = models.FileField()
    created_date = models.DateTimeField('date created', default=timezone.now)
    UserId = models.ForeignKey(users,on_delete=models.CASCADE)
    def __str__(self):
        return self.title 

class comment(models.Model):
    Comment = models.CharField(max_length=2000)
    create_at = models.DateTimeField('Date created')
    BlogId = models.ForeignKey(blogs,on_delete=models.CASCADE)
    user_id = models.ForeignKey(users,on_delete=models.CASCADE)
    def __str__(self):
        return self.Comment


class UserForm(ModelForm):
    class Meta:
        model = users
        fields = ["FirstName","LastName","UserMail","Password","image"]

class BlogForm(ModelForm):
    class Meta:
        model = blogs
        fields = ["title","sub_title","description","image","UserId"]
        


