from django.db import models
from Accounts.models import Profile

class Tasks (models.Model):
    STATUS_CHOICES = [
        ('todo',"To Do"),
        ('inprogress',"In Progress"),
        ('done',"Done"),
    ]

    PRIORITY_CHOICES = [
        ('low', "Low"),
        ('medium', "Medium"),
        ('high', "High"),
    ]

    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    discription = models.TextField(blank=True)
    status = models.CharField(max_length=10 , choices=STATUS_CHOICES, default="todo")
    priority = models.CharField(max_length=10 , choices=PRIORITY_CHOICES, default="medium")
    deadline = models.DateTimeField(null=True, blank=True)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

