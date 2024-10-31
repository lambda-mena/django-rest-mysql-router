from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, validators=[MinLengthValidator(5)])
    date = models.DateTimeField(auto_now_add=True)
    done = models.BooleanField(default=False, blank=True)
