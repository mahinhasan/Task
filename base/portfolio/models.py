from django.db import models

# Create your models here.

class Projects(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True,null=True)
    repository = models.CharField(max_length=350)

    def __str__(self) -> str:
        return self.title
    
    @property
    def my_fixed_repo(self):
        return "www.github.com/mahinhasan/django-api-project"