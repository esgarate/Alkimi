
# Register your models here.
from django.contrib import admin
from .models import Post #add this to import the Post model
from django.contrib.auth.models import Permission
admin.site.register(Post) #add this to register the Post model
