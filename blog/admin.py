from django.contrib import admin
from .models import BloggerInfo,PostBlog




@admin.register(BloggerInfo)
class JobPostedAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'created_at'
        
    )

@admin.register(PostBlog)
class JobPostedAdmin(admin.ModelAdmin):
    list_display = (
        'Author',
        'blog_content',
        'is_favorite'

        
    )
