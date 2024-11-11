from django.db import models
from django.utils import timezone


class Message(models.Model):
    content = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)
 