from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "task_manager_category"
        verbose_name = "Category"
        unique_together = ["name"]


class Task(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In progress"),
        ("pending", "Pending"),
        ("blocked", "Blocked"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    categories = models.ManyToManyField(Category, related_name="tasks")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks', null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task_manager_task"
        verbose_name = "Task"
        ordering = ["-created_at"]
        unique_together = ["title", "deadline"]


class SubTask(models.Model):
    STATUS_CHOICES = [
        ("new", "New"),
        ("in_progress", "In progress"),
        ("pending", "Pending"),
        ("blocked", "Blocked"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    task = models.ForeignKey(Task, related_name="subtasks", on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="new")
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subtasks', null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "task_manager_subtask"
        verbose_name = "SubTask"
        ordering = ["-created_at"]
        unique_together = ["title"]
