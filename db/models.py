from django.db import models


class Genre(models.models.Model):
    name = models.CharField(max_length=255)


class Actor(models.models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
