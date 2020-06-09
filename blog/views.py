from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .models import Post, Project
from .config import *
from .forms import ContactForm

#---------- Main Page ----------
#Main page w/ about me, blog, and contact form
def index(request):

    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    
    return render(request, 'blog/index.html', context)

#---------- About Me ----------
def about_me(request):
    return render(request, 'blog/about-me.html')


#---------- Contact Form ----------
#Sends contact form information to email address
def contact(request):

    if request.method == 'POST':

        form = ContactForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['name']
            contact_email = form.cleaned_data['email']
            message = ("Name: " + contact_name + 
                            "\nEmail: " + contact_email + 
                            "\n\nMessage: " + form.cleaned_data['message'])
            
            send_mail( contact_name + " sent you a message!", 
                    message, 
                    EMAIL, 
                    [EMAIL], 
                    fail_silently=False)

            return redirect('/')

    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form':form})

#---------- Projects Page ----------
#Page showcasing all projects, big & small
def projects(request):

    projects = Project.objects.all()
    
    context = {
        'projects': projects,
    }
    return render(request, 'blog/projects.html', context)

#---------- Post Detail Page ---------- 
#Displays details of blog post
def post_detail(request, slug):

    post = Post.objects.get(slug=slug)
    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)