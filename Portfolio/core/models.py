# from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Portfolio(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    mobile = models.CharField(max_length=15)
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.name