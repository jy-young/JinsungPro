from django.contrib import admin
from .models import Post

#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','product_photo']
    list_display_links = ['title']
    search_fields = ['title']