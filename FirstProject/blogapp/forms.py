from django.forms import ModelForm
from .models import users, blogs


class UserForm(ModelForm):
    class Meta:
        model = users
        fields = ["FirstName","LastName","UserMail","Password","image"]

class BlogForm(ModelForm):
    class Meta:
        model = blogs
        fields = ["title","sub_title","description","image","UserId"]