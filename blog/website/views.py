from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def helloBlog(request):
    return render(request, 'index.html', {'posts': Post.objects.filter(deleted=False)})

def postDetail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})

# Create your views here.
