from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Image(models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(blank=True, null=True, upload_to="images/")

    def __str__(self):
        return self.title

class Post(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    author = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    status = models.IntegerField(choices=STATUS, default=0)
    tags = TaggableManager()
    post_icon = models.ForeignKey(Image, on_delete=models.PROTECT, null=True, blank=True, default='')
    description = models.TextField(default='')
    content = models.TextField()
    popular = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class PostImage(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="posts/")

class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(default='')
    github_url = models.URLField(default='')
    project_url = models.URLField(default='')
    image = models.ImageField(blank=True, null=True, upload_to="projects/")
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.title

