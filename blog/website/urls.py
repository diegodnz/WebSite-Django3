from django.urls import path
from .views import helloBlog
from .views import postDetail

urlpatterns = [
    path('', helloBlog, name = 'homeBlog'),
    path('post/<int:id>/', postDetail, name = 'postDetail'),
]