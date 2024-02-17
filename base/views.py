from django.shortcuts import render
from django.http import HttpResponse

# render simple view to test
def taskList(request):
    #return HttpResponse("hello world!")
    return HttpResponse("To-Do List")
