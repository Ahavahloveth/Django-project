from django.urls import path
from . import views

# these are the urls for your music app
urlpatterns = [
    path("song/", views.SongList.as_view()),
    path("song/<int:pk>", views.SongDetail.as_view()),
    path("artiste/", views.ArtisteList.as_view()),
    path("artiste/<int:pk>", views.ArtisteDetail.as_view())
]