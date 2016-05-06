from django.contrib import admin

# import my Post class from models.py
from .models import Post


# Register your models here.
admin.site.register(Post)

