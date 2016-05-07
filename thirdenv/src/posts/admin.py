from django.contrib import admin

# import my Post class from models.py
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	
	list_display = ["__str__", "timestamp"]
	list_filter = ["title", "timestamp"]
	search_fields = ['title', 'content']
	#list_editable = ['title']

	class Meta:
		model = Post

# Register your models here.
admin.site.register(Post, PostModelAdmin)

