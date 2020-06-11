from django.contrib import admin
from .models import Post, Project, Content, Image


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_url', 'github_url')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'updated_on')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')

admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(Image, ImageAdmin)