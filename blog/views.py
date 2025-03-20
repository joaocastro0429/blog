from django.shortcuts import render
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects.all().order_by('-date_created')
    return render(request,'home.html',{'posts':posts})
