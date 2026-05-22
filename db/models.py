from django.db import models


class Genre(models.Model):  # <-- Corregido aquí de models.models.Model a models.Model
    name = models.CharField(max_length=255)


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
