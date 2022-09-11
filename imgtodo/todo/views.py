from django.shortcuts import render
from django.views.generic import ListView
from .models import Todo

class ListTodoView(ListView):
  template_name = 'todo/todo_list.html'
  model = Todo
