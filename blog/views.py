from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Post
from .config import *

#---------- Main Page ----------
#Main page w/ about me, blog, and contact form
def index(request):

    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    
    return render(request, 'blog/index.html', context)

#---------- Post Detail Page ---------- 
#Displays details of blog post
def post_detail(request, slug):

    post = Post.objects.get(slug=slug)
    context = {
        'post':post,
    }

    return render(request, 'blog/post_detail.html', context)

#---------- Projects Page ----------
#Page showcasing all projects, big & small
def projects(request):

    return render(request, 'blog/projects.html')

#---------- Contact Form ----------
#Sends contact form information to email address
def contact(request):

    if request.method == 'POST':
        form_data = request.POST.dict()
        name = form_data.get("name")
        email = form_data.get("email")
        message = "Name: " + name + "\nEmail: " + email + "\n\nMessage: " + form_data.get("message")

        send_mail( name + " sent you a message!", 
                    message, 
                    EMAIL, 
                    [EMAIL], 
                    fail_silently=False)
       
    return redirect('/')