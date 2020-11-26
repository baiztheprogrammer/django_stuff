from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.

def userlist(request):
    users = User.objects.all()
    return HttpResponse(users)

def bloglist(request):
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    return render(request,'firstapp/blog-template.html',context)

def postlist(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request,'firstapp/post.html',context)

def BlogDetailView(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    posts = blog.post_set.all()
    context = {'blog':blog,'posts':posts}
    return render(request,'firstapp/blog-detail.html',context)
