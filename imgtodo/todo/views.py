from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Todo

class ListTodoView(ListView):
  template_name = 'todo/todo_list.html'
  model = Todo

class CreateTodoView(CreateView):
  template_name = 'todo/todo_create.html'
  model = Todo
  fields = ('title', 'body', 'category')
  success_url = reverse_lazy('list-todo')
