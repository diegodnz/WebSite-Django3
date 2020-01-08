from django.shortcuts import render
from django.http import HttpResponse

def hello_blog(request):
    numeros = [1, 2, 3, 4, 5, 6, 7, 8]
    data = {'diego': 'diniz', 'numeros': numeros}
    return render(request, 'index.html', data)
# Create your views here.
