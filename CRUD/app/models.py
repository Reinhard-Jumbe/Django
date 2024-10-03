from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=60)
    adm_no = models.IntegerField(blank=False, null=False)
    email = models.EmailField()
    age = models.IntegerField()
    image = models.ImageField(upload_to='profiles', default='default.jpg')

    #any time u make changes to the models file u must make and run migrations

