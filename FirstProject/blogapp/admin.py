from django.contrib import admin
from .models import users, blogs, comment
# Register your models here.

class CommentInline(admin.TabularInline):
    model = comment
    extra = 0

class BlogAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]
    
admin.site.register(users)
admin.site.register(blogs,BlogAdmin)
admin.site.register(comment)