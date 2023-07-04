from django.db import models


# Create your models here.

class Ancient(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()

    def __str__(self):
        return self.title
    

