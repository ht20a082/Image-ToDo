from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from .models import Todo

class ListTodoView(ListView):
  template_name = 'todo/todo_list.html'
  model = Todo

class CreateTodoView(CreateView):
  template_name = 'todo/todo_create.html'
  model = Todo
  fields = ('title', 'body', 'priority', 'category')
  success_url = reverse_lazy('list-todo')

class DetailTodoView(DetailView):
  template_name = 'todo/todo_detail.html'
  model = Todo

class DeleteTodoView(DeleteView):
  template_name = 'todo/todo_delete.html'
  model = Todo
  success_url = reverse_lazy('list-todo')

class UpdateTodoView(UpdateView):
  model = Todo
  fields = ('title', 'body', 'priority', 'category')
  template_name = 'todo/todo_update.html'
  success_url = reverse_lazy('list-todo')

