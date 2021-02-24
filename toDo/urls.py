from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:pk>/', views.ToDoView.as_view()),
    path('all/', views.getAllView.as_view()),
    path('create/', views.ToDoCreateView.as_view())
]
