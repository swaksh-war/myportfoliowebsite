from django.db import models

# Create your models here.

class Education(models.Model):
    name = models.CharField(max_length=255, default='No data')
    degree = models.CharField(max_length=255, default='No data')
    started_year = models.PositiveIntegerField()
    ender_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=255, default='No data')
    description = models.TextField()
    started_date = models.DateField()
    ended_date = models.DateField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    company_name = models.CharField(max_length=255, default='No data')
    company_post = models.CharField(max_length=255, default='No data')
    work_description = models.TextField()
    started_from = models.DateField()
    worked_till = models.DateField()

    def __str__(self):
        return self.company_name

class Blog(models.Model):
    title = models.CharField(max_length=255, default='Default title')
    content = models.TextField()

    def __str__(self):
        return self.title

    