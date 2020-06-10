from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    updated_on = models.DateTimeField(auto_now= True)
    description = models.TextField(default='')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(default='')
    github_url = models.URLField(default='')
    project_url = models.URLField(default='')
    image = models.ImageField(blank=True, null=True, upload_to="projects/")

    def __str__(self):
        return self.title

class Content(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.title