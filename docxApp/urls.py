from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.MovieListView.as_view()),
    path("form/", views.Template.as_view()),
]
