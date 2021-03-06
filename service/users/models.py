from django.db import models
from uuid import uuid4


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(unique=True, max_length=64)

    def __str__(self):
        return f"User object(UName: {self.user_name}, EMail: {self.email})"
