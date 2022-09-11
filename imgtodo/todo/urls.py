from django.urls import path
from . import views

urlpatterns = [
  path('todo/', views.ListTodoView.as_view(), name='list-todo'),
  path('todo/create/', views.CreateTodoView.as_view(), name='create-todo'),
]