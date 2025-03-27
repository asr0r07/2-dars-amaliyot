from django.db import models
from django.utils.text import slugify
from author.base_models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
