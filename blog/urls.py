from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    #path('post/', views.post_detail, name='post_detail')
    path('<slug:slug>/', views.post_detail, name='post_detail')
]