from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)