from django.conf import settings
from django.db import models


class HomePage(models.Model):
    "Generated Model"
    body = models.TextField()


class CustomText(models.Model):
    "Generated Model"
    title = models.CharField(
        max_length=150,
    )
