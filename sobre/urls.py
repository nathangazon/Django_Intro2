from django.urls import path

from . import views

# /blog/posts
urlpatterns = [
    path('teste/', views.teste)
]
