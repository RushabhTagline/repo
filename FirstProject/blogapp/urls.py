from urllib.parse import urlunparse
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.indexpage,name='indexpage'),
    path('loginpage/',views.loginpage,name='loginpage'),
    path('ragi/',views.RegistrationPage,name='RegistrationPage'),
    path('Logout/',views.logout,name='logout'),
    path('blogspage/',views.Blogspage,name='Blogspage'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
