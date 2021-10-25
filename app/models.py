from django.db import models
from django.contrib.auth.models import User

class UserChore(models.Model):
    name=models.CharField(max_length=50)
    
    class Meta:
        verbose_name='UserChore'
        verbose_name_plural='UserChores'
    
    def __str__(self):
        return self.name


class Chore(models.Model):

    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    imagen=models.ImageField(upload_to="app", null=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    userchore=models.ManyToManyField(UserChore)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)
    StartTask=models.DateTimeField(auto_now_add=True)
    CompletedTask=models.DateTimeField(auto_now=True)
    #duration=models.DurationField()

    class Meta:
        verbose_name='chore'
        verbose_name_plural='chores'
    
    def __str__(self):
        return self.name

