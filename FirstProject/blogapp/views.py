from urllib import request
from webbrowser import get
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render 
from blogapp.models import UserForm, BlogForm
from blogapp.models import users, blogs
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def indexpage(request):
    User = 0
    image = ""
    if 'User_id' in request.session:
        user = request.session['User_id']
        data = users.objects.filter(id=user).get()
        User = user
        image = data.image
    text = "Hello..!",
    return render(request,'index.html',{'text':text,'id':User,'image':image})

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
            request.session['User_id'] = user_id
            return redirect('/')
    return render(request,'login.html',{'msg':msg})

def logout(request):
    del request.session['User_id']
    return redirect('/')

def Blogspage(request):
    if 'User_id' in request.session:
        user = request.session['User_id']
        data = users.objects.filter(id=user).get()
        image = data.image
    blog = blogs.objects.all().order_by('-id')
    paginator = Paginator(blog, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request,'blogs.html',{'blogs':page_obj,"image":image})

def AddNewBlog(request):
    frm = BlogForm  
    if 'save' in request.POST:
        UserId = request.session['User_id']
        data = BlogForm(request.POST,request.FILES)
        data.save()
        return redirect('/blogspage')
    return render(request,'AddBlog.html',{'frm':frm})
