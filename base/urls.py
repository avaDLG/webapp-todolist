from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate

urlpatterns = [
    # needd .as_view urls cannot use class inside it but can use a function
    path('', TaskList.as_view(), name='tasks'),

    # number the tasks by integer values
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),

    path('task-create/', TaskCreate.as_view(), name='task-create'),
]

