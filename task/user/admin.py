from django.contrib import admin
from .models import User_model,Post_model
# Register your models here.

admin.site.register(User_model)
admin.site.register(Post_model)
