from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

# routing url for each view
urlpatterns = [
    # needd .as_view urls cannot use class inside it but can use a function
    path('', TaskList.as_view(), name='tasks'),

    # number the tasks by integer values
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),

    path('task-create/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', TaskDelete.as_view(), name='task-delete'),
    
]   


