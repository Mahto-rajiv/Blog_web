from django.contrib import admin
from blog.models import * 

class post_display(admin.ModelAdmin):
    list_display = ['id', 'author', 'date_posted']

admin.site.register(Post, post_display)