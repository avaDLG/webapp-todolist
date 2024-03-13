from django.urls import path
from .views import taskList

urlpatterns = [
    # needd .as_view urls cannot use class inside it but can use a function
    path('', taskList.as_view().taskList, name='tasks'),
]

