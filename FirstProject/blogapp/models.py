from dataclasses import field, fields
from django.utils import timezone
import email
from email.mime import image
from django.db import models
from django.forms import ModelForm, PasswordInput

# Create your models here.

class users(models.Model):
    FirstName = models.CharField(max_length=250)
    LastName = models.CharField(max_length=250)
    UserMail = models.EmailField(max_length=100)
    Password = models.CharField(max_length=15)
    image = models.FileField()
    def __str__(self):
        return self.FirstName + self.LastName + '(' + self.UserMail + ')'

class blogs(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    image = models.FileField()
    UserId = models.ForeignKey(users,on_delete=models.CASCADE)
    def __str__(self):
        return self.title 

class UserForm(ModelForm):
    class Meta:
        model = users
        fields = ["FirstName","LastName","UserMail","Password","image"]

class BlogForm(ModelForm):
    class Meta:
        model = blogs
        fields = ["title","sub_title","description","image","UserId"]
        


