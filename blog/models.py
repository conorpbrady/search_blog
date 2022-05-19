from django.db import models
from django.utils import timezone

# Create your models here.

class Posts(models.Model):

    post_date = models.DateTimeField(default = timezone.now)
    subject = models.CharField(max_length = 255)
    post = models.TextField()

