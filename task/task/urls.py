from django.contrib import admin
from django.urls import path,include



urlpatterns = [
   path('',include('user.urls')),
    path('admin/', admin.site.urls),
    # path('<slug:slug>/', post_detail, name='post_detail'),
]
