from django.db import models
from django.db.models import Model

# Create your models here.
class feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    content=models.TextField()

    def __str__(self):
        return self.name