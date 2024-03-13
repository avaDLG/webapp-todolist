from django.urls import path
from .views import TaskList

urlpatterns = [
    # needd .as_view urls cannot use class inside it but can use a function
    path('', TaskList.as_view(), name='tasks'),
]

