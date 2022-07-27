from xml.etree.ElementTree import Comment
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from django.utils import timezone
from .models import UserForm, BlogForm
from .models import users, blogs, comment  
from django.core.paginator import Paginator

# Create your views here.

def indexpage(request):
    if 'User_id' in request.session:
        user = request.session['User_id']
        data = users.objects.filter(id=user).get()
        image = data.image
        user = request.session['User_id']
        return render(request,'index.html',{'id':user, 'image':image, 'UserId':user})
    return render(request,'index.html',{})

def RegistrationPage(request):
    frm = UserForm  
    if 'save' in request.POST:
        data = UserForm(request.POST,request.FILES)
        if data.is_valid():   
            data.save()
            return redirect('/loginpage')
    return render(request,'registration.html',{'frm':frm})

def loginpage(request):
    msg = ""
    if 'login' in request.POST:
        email = request.POST['mail']
        password = request.POST['password']
        data = users.objects.filter(UserMail=email, Password=password)
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
    blog = blogs.objects.order_by('-created_date')
    paginator = Paginator(blog, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'blogs.html',{'page_obj':page_obj})

def AddNewBlog(request):
    frm = BlogForm  
    if 'save' in request.POST:
        data = BlogForm(request.POST,request.FILES)
        if data.is_valid():    
            data.save()
        return redirect('/blogspage')
    return render(request, 'AddBlog.html',{'frm':frm})

def BlogDetailsPage(request,blog_id):
    data = blogs.objects.filter(id=blog_id).get()
    pk = data.UserId.id
    comments = comment.objects.filter(BlogId=blog_id).order_by('create_at')
    
    if 'post' in request.POST:
        comments = request.POST['CommentInput']  
        userid = users.objects.filter(id=request.session['User_id']).get()
        timeat = timezone.now()
        datasave = comment(Comment=comments, create_at=timeat, BlogId=data, user_id=userid)
        datasave.save()
        return redirect('/blog/blogdetails/')
    return render(request, 'Blog-Details.html',{'data':data, 'pk':pk, 'comments':comments})
    
def AuthorDetailsPage(request,pk):
    authordata = users.objects.filter(id=pk).get()
    blog = blogs.objects.filter(UserId=authordata.id).order_by('-created_date')
    return render(request, 'Author-DetaisPage.html',{'AuthorData':authordata, 'blog':blog, 'pk':authordata.id})

def BloggersPage(request):
    blogger = users.objects.all()
    return render(request,'bloggers.html',{'bloggers':blogger})
    
