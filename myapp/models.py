from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=50)  

    def __str__(self):
        return self.name

class Education(models.Model):
    school = models.CharField(max_length=150)
    course = models.CharField(max_length=150)
    year = models.CharField(max_length=20)

    def __str__(self):
        return self.school

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
