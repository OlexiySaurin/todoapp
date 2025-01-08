from django.db import models
from django.contrib.auth.models import User


class SimpleTask(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    due_date = models.DateField(blank=True, null=True)
    priority = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.title
