from django.contrib import admin
from .models import Post, Contact


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'approved']
    search_fields = ['title', 'subtitle', 'content']
    #fields = ['title', 'subtitle', 'content']

    #def get_queryset(self, request):
        #return Post.objects.filter(deleted=False)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
    search_fields = ['name', 'email', 'message']

admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)
# Register your models here.
