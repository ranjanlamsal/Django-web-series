from django.urls import path,include
from . import views

urlpatterns= [
    path('postHome/', views.postHome), #127.0.0.1:8000/post/postHome
    path('', views.viewAll), #127.0.0.1:8000/post/
]