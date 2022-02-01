from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class ToDo(models.Model):
    type = (
        ('Active', 'Active'),
        ('Soon', 'Soon'),
        ('Done', 'Done'),
    )
    title = models.CharField(max_length=30)
    time = models.DateTimeField()
    place = models.CharField(max_length=30)
    description = models.CharField(max_length=60)
    status = models.CharField(max_length=10, choices=type)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, {self.time}, {self.status}'