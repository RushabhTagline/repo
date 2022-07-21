import email
import logging
from urllib import request
from xml.dom.minidom import Document
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogapp.models import UserForm

from blogapp.models import users

# Create your views here.

def indexpage(request):
    # tempplate = loader.get_template('index.html')
    User = 0
    if 'User_id' in request.session:
        user = request.session['User_id']
        User = user
    text = "Hello..!",
    
    # return HttpResponse(tempplate.render(context,request))
    return render(request,'index.html',{'text':text,'id':User})

def RegistrationPage(request):
    msg = ""
    # if 'save' in request.POST:
    #     fname = request.POST['fname']
    #     lname = request.POST['lname']
    #     mail = request.POST['mail']
    #     password = request.POST['password']
    #     confirm_password = request.POST['c_password']
    #     if password != confirm_password:
    #         msg = "Enter valid password..!"
    #     else:
    #         data = users(FirstName=fname,LastName=lname,UserMail=mail,Password=password,ConfirmPassword=confirm_password)
    #         data.save()
    #         return redirect('/blog')

    frm = UserForm
    if 'save' in request.POST:
        data = UserForm(request.POST,request.FILES)
        data.save()
        return redirect('/loginpage')

    return render(request,'registration.html',{'msg':msg,'frm':frm})

def loginpage(request):
    msg = ""
    if 'login' in request.POST:
        Email = request.POST['mail']
        password = request.POST['password']
        data = users.objects.filter(UserMail=Email,Password = password)
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
    
