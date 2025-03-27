from django.db import models
from .base_models import BaseModel


class Author(BaseModel):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    bio = models.TextField()

    def __str__(self):
        return self.name