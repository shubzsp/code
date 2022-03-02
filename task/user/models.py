from django.db import models

# Create your models here.
class User_model(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField(blank=True)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self):
    
        return self.first_name
    
class Post_model(models.Model):
    user=models.ForeignKey(User_model,on_delete=models.CASCADE)
    updated_at=models.TimeField( auto_now=True)
    text=models.CharField(max_length=100)
    created_at=models.TimeField( auto_now_add=True)
    class Meta:
        managed=False
    
    
    