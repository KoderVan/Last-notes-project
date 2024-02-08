from django.db import models
from django.contrib.auth.models import User


class Notes(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True)
    title = models.CharField(max_length=200, blank=True)
    content = models.TextField(max_length=500, blank=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
