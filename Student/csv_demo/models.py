from django.db import models

# Create your models here.


class Examination(models.Model):
    rollnumber = models.CharField(max_length=100)
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    marks = models.CharField(max_length=100)

    def __str__(self):
        return self.first
