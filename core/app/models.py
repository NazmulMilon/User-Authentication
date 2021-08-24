from django.db import models

# Create your models here.
class Mainuser(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=50)
    phone=models.IntegerField()
    images=models.ImageField(upload_to='main',blank=True)
    def __str__(self):
        return self.name