from django.db import models
from django.shortcuts import render

CHOICES = [
        ('Industrial', 'Industrial'),
        ("Medical", 'medical'),
        ("agricultural", 'agricultural'),
        ("ُEducation", 'Education'),
       
    ]

class Project(models.Model):
    name = models.CharField(max_length=100)
    sector=models.CharField(max_length=40 , choices=CHOICES , default=None)
    description = models.TextField()
    fund=models.CharField(max_length=100)


    def __str__(self):
        return self.name
