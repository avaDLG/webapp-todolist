from django.shortcuts import render
#from django.http import HttpResponse

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Task

# I will be using class based views

class TaskList(ListView): # to see all items
    model = Task 
    # default is object_list
    # more apt name for objects within class
    context_object_name = 'tasks'

class TaskDetail(DetailView): # returning information about specific task
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html' # instead of using task_detail.html

class TaskCreate(CreateView): # to create task
    model = Task
    fields = '__all__' # want all fields
    success_url = reverse_lazy('tasks') # redirect user to tasks after creating item

