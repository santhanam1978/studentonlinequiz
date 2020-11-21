from django.db import models
from django.urls import reverse

# Create your models here.
class Mymodel(models.Model):
    question=models.CharField(max_length=1000)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    anwers=models.CharField(max_length=100)
    class Meta:
        db_table='onlinequiz'
    def get_obsolute_urls(self):
        return reverse('index')

