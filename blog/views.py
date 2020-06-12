from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from .models import Post, Project, Content, Image
from .config import *
from .forms import ContactForm

#---------- Main Page ----------
#Main page w/ about me, blog, and contact form
def index(request):

    posts = Post.objects.all().order_by('-created_on')

    context = {
        'posts': posts,
    }
    
    return render(request, 'blog/index.html', context)

#---------- About ----------
def about(request):

    content = Content.objects.get(title='About')
    photo = Image.objects.get(title='Me')

    context = {
        'content': content,
        'photo':photo,
    }

    return render(request, 'blog/about.html', context)


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

    content = Content.objects.get(title='Contact');
    
    context = {
        'content':content,
        'form':form,
    }

    return render(request, 'blog/contact.html', context)

#---------- Portfolio Page ----------
#Page showcasing all projects, big & small
def portfolio(request):

    content = Content.objects.get(title='Portfolio')
    projects = Project.objects.all().order_by('order')

    context = {
        'content': content,
        'projects': projects,
    }
    return render(request, 'blog/portfolio.html', context)

#---------- Post Detail Page ---------- 
#Displays details of blog post
def post_detail(request, slug):

    post = Post.objects.get(slug=slug)

    context = {
        'post': post,
    }

    return render(request, 'blog/post_detail.html', context)

#--------- Tag Detail ----------
#Displays posts associated w/ clicked tags
def tag_detail(request, slug):

    posts = Post.objects.filter(tags__slug__in=[slug])

    context = {
      'posts':posts,
    }

    return render(request, 'blog/index.html', context)





