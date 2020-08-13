from django.db import models

# Create your models here.
class User_Forms(models.Model):
    title=models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title