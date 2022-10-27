from authentication.models import User
from django.db import models

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos', null=True)
    title = models.CharField(max_length = 120)
    description = models.TextField()
    completed = models.BooleanField(default = False)

    def __str__(self):
        return self.title
