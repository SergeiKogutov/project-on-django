from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('title', max_length=50)
    task = models.TextField('task')
    status = models.TextField('status', max_length=50)
    priority = models.CharField('priority', max_length=50)
    deadlines = models.DateTimeField('deadlines', max_length=50)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
