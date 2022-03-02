from django.shortcuts import render,get_object_or_404
from .models import Post_model
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.
def home(request):

    context={
        'posts':Post_model.objects.all()
    }
    return render(request,'blog/home.html',context)


class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post_model
    fields = ['title','content']
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


