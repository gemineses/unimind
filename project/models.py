from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# Topic List
class Topic(models.Model):
    parent_topic = models.ForeignKey(to='Topic', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)


# Proyect Properties
class Project(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateTimeField('date published', null=True)

# Proyect Task
class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created')

