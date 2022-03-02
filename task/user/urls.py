
from django.urls import path
from . import views
from .views import (
   
    PostCreateView,
    
)
urlpatterns=[
 
    path('post/new/', PostCreateView.as_view(),name='post-create'), 
  
    path('home',views.home,name="blog-about"),
]