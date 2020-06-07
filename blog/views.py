from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import Post
from .config import *

#Main index page
def index(request):

    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    
    return render(request, 'blog/index.html', context)

#Post detail page w/ the full blog post
def post_detail(request, slug):

    post = Post.objects.get(slug=slug)
    context = {
        'post':post,
    }

    return render(request, 'blog/post_detail.html', context)

#Submitting our contact form leads here and sends an email with the info
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