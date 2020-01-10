from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'deleted']
    search_fields = ['title', 'subtitle', 'content']
    #fields = ['title', 'subtitle', 'content']

    #def get_queryset(self, request):
        #return Post.objects.filter(deleted=False)
admin.site.register(Post, PostAdmin)
# Register your models here.
