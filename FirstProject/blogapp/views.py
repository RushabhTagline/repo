import email
import logging
from urllib import request
from xml.dom.minidom import Document
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogapp.models import UserForm

from blogapp.models import users, Blogs

# Create your views here.

def indexpage(request):
    User = 0
    if 'User_id' in request.session:
        user = request.session['User_id']
        User = user
    text = "Hello..!",
    return render(request,'index.html',{'text':text,'id':User})

def RegistrationPage(request):
    frm = UserForm  
    if 'save' in request.POST:
        data = UserForm(request.POST,request.FILES)
        data.save()
        return redirect('/loginpage')
    return render(request,'registration.html',{'frm':frm})

def loginpage(request):
    msg = ""
    if 'login' in request.POST:
        Email = request.POST['mail']
        Password = request.POST['password']
        data = users.objects.filter(UserMail=Email,Password = Password)
        if (data.count()==0):
            msg = "Invalid Email OR Password";          
        else:
            user = data.get();
            user_id = user.id
            request.session['User_id']= user_id
            return redirect('/')
    return render(request,'login.html',{'msg':msg})

def logout(request):
    del request.session['User_id']
    return redirect('/')

def Blogspage(request):
    blog = Blogs.objects.all()
    return render(request,'blogs.html',{'blogs':blog})
    
