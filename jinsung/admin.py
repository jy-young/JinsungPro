from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin

#admin.site.register(Post)

#@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ['id','title','product_photo']
    list_display_links = ['title']
    search_fields = ['title']
    summernote_fields = ('content')
admin.site.register(Post, PostAdmin)