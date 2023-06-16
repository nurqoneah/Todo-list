from django.db import models
from datetime import datetime

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    time = models.DateTimeField(default=datetime.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    


