from django.contrib import admin
from .models import Task

# resgistering model Task with admin panel
admin.site.register(Task)
