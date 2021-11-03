from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class Event(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField('Event Name', max_length=20)
    event_date=models.DateTimeField('Event')
    #venue=models.ForeignKey(Venue, blank=True)
    #manager=models.ForeignKey(User, blank=True)
    description=models.TextField(blank=True)
    #attendess=models.ManyToManyField(MyClu)

    def __str__(self):
        return self.name


class UserChore(models.Model):
    name=models.CharField(max_length=50)
    lastName=models.CharField(max_length=50)
    gener=models.CharField(max_length=10)
    
    class Meta:
        verbose_name='UserChore'
        verbose_name_plural='UserChores'
        ordering=['name']
    
    def __str__(self):
        return self.name


class Chore(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to="app", null=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    userchore=models.ManyToManyField(UserChore)
    created=models.DateTimeField('Created date', auto_now_add=True)
    updated=models.DateTimeField('Updated date', auto_now_add=True)
    #StartTask=models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    #timestamp=models.DateField(auto_now_add=True, auto_now=False, blank=True)
    #CompletedTask=models.DateTimeField(auto_now=True)
    #duration=models.DurationField()

    class Meta:
        verbose_name='chore'
        verbose_name_plural='chores'
        ordering=['name']
    
    def __str__(self):
        return self.name

