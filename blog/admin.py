from django.contrib import admin
from .models import Post, Project, Content


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_url', 'github_url')

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'updated_on')

admin.site.register(Post, PostAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Content, ContentAdmin)