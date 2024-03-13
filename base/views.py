# views.py is what the user sees

from django.shortcuts import render
#from django.http import HttpResponse

# premade django generic list 
from django.views.generic.list import ListView
from .models import Task

# render simple view to test
# inherit ListView
class TaskList(ListView):
    model = Task 

