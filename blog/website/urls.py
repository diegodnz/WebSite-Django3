from django.urls import path
from .views import homeBlog, postDetail, saveForm

urlpatterns = [
    path('', homeBlog, name = 'home'),
    path('post/<int:id>/', postDetail, name = 'postDetail'),
    path('200/', saveForm, name = 'saveForm')
]