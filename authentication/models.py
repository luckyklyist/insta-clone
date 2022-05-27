from django.db import models

# Create your models here.
class signup(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    password1=models.CharField(max_length=100)
    password2=models.CharField(max_length=100)

    def __str__(self):
        return self.username