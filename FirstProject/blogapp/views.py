from random import randint
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import send_mail
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
            return redirect('/blog/loginpage')
    return render(request,'registration.html',{'frm':frm})

def loginpage(request):
    msg = ""
    if 'login' in request.POST:
        email = request.POST['mail']
        password = request.POST['password']
        data = users.objects.filter(UserMail=email, Password=password)
        
        if not data:
            msg = "Invalid Email OR Password";          
        else:
            request.session['email'] = email 
            otp = randint(100000,999999)
            send_mail(
                'This is my subject',
                'OTP is : '+str(otp),
                'rushabh.tagline@gmail.com',
                ['' +str(email)],
                fail_silently=False,
            )
            data.update(otp=otp)
            return redirect('/verificationpage')
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
    if 'Blog_id' in request.session:
        del request.session['Blog_id']
    data = blogs.objects.filter(id=blog_id).get()
    pk = data.UserId.id
    comments = comment.objects.filter(BlogId=blog_id).order_by('create_at')
    return render(request, 'Blog-Details.html',{'data':data, 'pk':pk, 'comments':comments})

def addcomment(request,blog_id):
    if 'Blog_id' in request.session:
        del request.session['Blog_id']
    msg = ""
    if 'User_id' in request.session:
        data = blogs.objects.filter(id=blog_id).get()
        if 'post' in request.POST:
            comments = request.POST['CommentInput']  
            userid = users.objects.filter(id=request.session['User_id']).get()
            datasave = comment(Comment=comments, create_at=timezone.now(), BlogId=data, user_id=userid)
            datasave.save()
            return redirect(f'/blogdetails/{blog_id}')
    else:
        msg = "Please login"    
        request.session['Blog_id'] = blog_id
    return render(request,'New-comment.html',{'msg':msg})
    
def AuthorDetailsPage(request,pk):
    authordata = users.objects.filter(id=pk).get()
    blog = blogs.objects.filter(UserId=authordata.id).order_by('-created_date')
    return render(request, 'Author-DetaisPage.html',{'AuthorData':authordata, 'blog':blog, 'pk':authordata.id})

def BloggersPage(request):
    blogger = users.objects.all()
    return render(request,'bloggers.html',{'bloggers':blogger})
     

def VerificationPage(request):
    msg = ""
    if 'Verified' in request.POST:
        s_email = request.session['email']
        userData = users.objects.filter(UserMail = s_email).get()
        user_enter_otp = request.POST['OTP']
        if(user_enter_otp != str(userData.otp)):
            msg = "Invalid otp"
        else:
            user_id = userData.id
            request.session['User_id'] = user_id
            del request.session['email']
            if 'Blog_id' in request.session:
                blog_id = request.session['Blog_id']
                return redirect(f'/blogdetails/{blog_id}')
            else:
                return redirect('/blog')
    return render(request,'verification.html',{'msg':msg})


