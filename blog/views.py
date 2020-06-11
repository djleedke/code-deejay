from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .models import Post, Project, Content
from .config import *
from .forms import ContactForm

#---------- Main Page ----------
#Main page w/ about me, blog, and contact form
def index(request):

    posts = Post.objects.all()
    tags = Post.tags.all()

    context = {
        'posts': posts,
        'tags':tags,
    }
    
    return render(request, 'blog/index.html', context)

#---------- About Me ----------
def about_me(request):

    about_me = Content.objects.get(title='About Me')
    tags = Post.tags.all()

    context = {
        'about_me': about_me,
        'tags': tags,
    }
    return render(request, 'blog/about-me.html', context)


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

    tags = Post.tags.all()
    
    context = {
        'form':form,
        'tags':tags,
    }

    return render(request, 'blog/contact.html', context)

#---------- Projects Page ----------
#Page showcasing all projects, big & small
def projects(request):

    projects = Project.objects.all()
    tags = Post.tags.all()

    context = {
        'projects': projects,
        'tags':tags,
    }
    return render(request, 'blog/projects.html', context)

#---------- Post Detail Page ---------- 
#Displays details of blog post
def post_detail(request, slug):

    post = Post.objects.get(slug=slug)
    tags = Post.tags.all()

    context = {
        'post': post,
        'tags':tags,
    }

    return render(request, 'blog/post_detail.html', context)