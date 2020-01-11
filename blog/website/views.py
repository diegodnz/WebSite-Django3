from django.shortcuts import render
from .models import Post, Contact

def homeBlog(request):
    return render(request, 'index.html', {'posts': Post.objects.filter(approved=True)})

def postDetail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})

def saveForm(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        if name != '' and email != '' and message != '':
            Contact.objects.create(
                name = name,
                email = email,
                message = message
            )
            return render(request, 'contact.html')
        else:
            return render(request, 'falsecontact.html')
    else:
        return render(request, 'index.html')

# Create your views here.
