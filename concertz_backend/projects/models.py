from django.db import models
import uuid

class Project(models.Model):
    project_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    concert = models.ForeignKey('events.Concert', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    details = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    expires_on = models.DateTimeField(null=True)

class Team(models.Model):
    teamate_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    employee = models.ForeignKey('accounts.EmployeeProfile', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    joined_on = models.DateTimeField(auto_now_add=True)
    duration = models.IntegerField()

class Task(models.Model):
    task_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    employee = models.ForeignKey('accounts.EmployeeProfile', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.BooleanField(default=False)