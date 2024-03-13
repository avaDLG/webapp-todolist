from django.shortcuts import render
#from django.http import HttpResponse


# I will be using class based views


from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True # redirect if should not be on page

    def get_success_url(self):
        return reverse_lazy('tasks')

class TaskList(LoginRequiredMixin, ListView): # to see all items
    model = Task 
    # default is object_list
    # more apt name for objects within class
    context_object_name = 'tasks'

    # so user can only access their data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user) # see their items
        context['count'] = context['tasks'].filter(complete=False).count() # see count of incomplete items

        return context 

class TaskDetail(LoginRequiredMixin, DetailView): # returning information about specific task
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html' # instead of using task_detail.html

class TaskCreate(LoginRequiredMixin, CreateView): # to create task
    model = Task
    fields = ['title', 'description', 'complete'] 
    success_url = reverse_lazy('tasks') # redirect user to tasks after creating item

    # can only create tasks for their user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView): # update item properties
    model = Task
    fields = ['title', 'description', 'complete'] 
    success_url = reverse_lazy('tasks') # redirect user to tasks after updating item

class TaskDelete(LoginRequiredMixin, DeleteView): # to delete item
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks') # redirect user to tasks after deleting item

