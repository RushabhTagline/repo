from dataclasses import field, fields
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

class blogs(models.Model):
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('Date published')
    image = models.FileField()

class UserForm(ModelForm):
    class Meta:
        model = users
        fields = ["FirstName","LastName","UserMail","Password","image"]
