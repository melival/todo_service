from django.db import models
from uuid import uuid4


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    user_name = models.CharField(max_length=64)
    email = models.CharField(unique=True, max_length=64)