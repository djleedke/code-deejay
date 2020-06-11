from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('about-me/', views.about_me, name='about_me'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('tags/<slug:slug>/', views.tag_detail, name='tag_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]