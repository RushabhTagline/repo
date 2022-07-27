from django.contrib import admin
from .models import users, blogs, comment
# Register your models here.

admin.site.register(users)
admin.site.register(blogs)
admin.site.register(comment)
