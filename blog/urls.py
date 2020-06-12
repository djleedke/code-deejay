from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('tags/<slug:slug>/', views.tag_detail, name='tag_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]