from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle', 'content']
    search_fields = ['title', 'subtitle', 'content']
    fields = ['title', 'subtitle', 'content']
admin.site.register(Post, PostAdmin)
# Register your models here.
