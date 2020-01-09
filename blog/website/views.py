from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def hello_blog(request):
    data = {'posts': Post.objects.all()}
    return render(request, 'index.html', data)
# Create your views here.
