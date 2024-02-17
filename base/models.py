from django.db import models
from django.contrib.auth.models import User

# creating database structure

# database table made into a model
class Task(models.Model):
    # attributes

    # authentication default in django
    # one to many realation ship (one user can have many tasks)
    # if user gets deleted all tasks will get deleted 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) 

    # upper limit on characters of title of task
    title = models.CharField(max_length=200)

    # text box for description of task
    description = models.TextField(null=True, blank=True)

    # by default the task will not be completed
    complete = models.BooleanField(default=False)

    # automatically record date in time when task created
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self): # string represteation/name of model
        return self.title

    class Meta:
        # complete tasks should be send to end of list 
        ordering = ['complete']
