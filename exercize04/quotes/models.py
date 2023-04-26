from django.db import models


class quote(models.Model):
    author = models.CharField(max_length=50)
    quote = models.CharField(max_length=50)
    context = models.CharField(max_length=50)
    source = models.CharField(max_length=50)
    create_at = models.DateField(auto_now=True)
    