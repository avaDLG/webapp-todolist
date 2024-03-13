from django.shortcuts import render
#from django.http import HttpResponse

# premade django generic list 
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

class TaskList(ListView):
    model = Task 

    # default is object_list
    # more apt name for objects within class
    context_object_name = 'tasks'

# returning information about specific task
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'

    # instead of using task_detail.html
    template_name = 'base/task.html'