from django.db import models
from django.urls import reverse


class ChoseType(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse('choseType', kwargs={'type' : self.pk})

class GlobalList(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    is_published = models.BooleanField(default=True)
    type = models.ForeignKey(ChoseType, on_delete=models.PROTECT)

    def __str__(self):
        return self.name