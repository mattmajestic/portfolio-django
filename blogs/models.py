from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags

from django.utils import timezone
from taggit.managers import TaggableManager
from mdeditor.fields import MDTextField


class PublishedManager(models.Manager):
    def ger_queryset(self):
        return super(PublishedManager, self).ger_queryset().filter(status=1)

# Create your models here.
STATUS = (
    (0, "Draft"),
    (1, "Published")
)

