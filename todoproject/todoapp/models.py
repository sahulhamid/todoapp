from django.db import models
from django.utils import timezone

# Create your models here.
class TaskForm(models.Model):
    task = models.CharField(max_length=100)
    compeleted = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.task
