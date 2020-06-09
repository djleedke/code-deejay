from django.contrib import admin
from .models import Post, Project


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_url', 'github_url')

admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)