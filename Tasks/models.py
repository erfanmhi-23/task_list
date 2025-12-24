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
    discription = models.models.TextField(blank=True)