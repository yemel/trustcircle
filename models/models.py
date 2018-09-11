from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Circle(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=100)


class Membership(models.Model):
    user = models.ForeignKey(User)
    circle = models.ForeignKey(Circle)
