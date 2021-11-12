from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from ckeditor.fields import RichTextField


class UserChore(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField('Username', max_length=50, null=False, blank=False)
    lastName=models.CharField(max_length=50, null=False, blank=False)
    email=models.EmailField('Email', blank=False, null=False)
    state=models.BooleanField('User', default=True)
    fecha_creacion=models.DateField('Fechad de Creacion', auto_now=False, auto_now_add=True)
    gener=models.CharField(max_length=10)
    
    class Meta:
        verbose_name='UserChore'
        verbose_name_plural='UserChores'
        ordering=['name']
    
    def __str__(self):
        return "{0},{1}".format(self.name, self.lastName)


class Chore(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField('Chore name', max_length=100, null=False, blank=False)
    #description=models.CharField('Description', max_length=200)
    content=RichTextField('Content', blank=True, null=True)
    imagen=models.ImageField(upload_to="app", null=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    userchore=models.ManyToManyField(UserChore)
    created=models.DateTimeField('Created date', auto_now=False, auto_now_add=True)
    updated=models.DateTimeField('Updated date', auto_now=False, auto_now_add=True)
    state=models.BooleanField('Active/Inactive', default=True)
    start_task=models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)
    #duration=models.DurationField()
    #timestamp=models.DateField(auto_now_add=True, auto_now=False, blank=True)
    #CompletedTask=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name='chore'
        verbose_name_plural='chores'
        ordering=['name']
    
    def __str__(self):
        return self.name



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