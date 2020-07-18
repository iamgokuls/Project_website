from django.db import models
from django.db.models import Model

# Create your models here.
class feedback(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    content=models.TextField()

    def __str__(self):
        return self.name
        
class history(models.Model):
    email=models.EmailField()
    message=models.CharField(max_length=120)
    datetime= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    