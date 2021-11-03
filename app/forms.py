from django import forms
#from django.db.models.base import Model
from django.forms import fields, widgets, ModelForm
from .models import UserChore, Chore


class UserChoreForm(forms.ModelForm):
    class Meta:
        model=UserChore
        fields=['name', 'lastName', 'gener']


class ChoreForm(forms.ModelForm):
    class Meta:
        model=Chore
        fields=['name', 'description', 'author']


class myform(forms.Form):
    name=forms.CharField(label='Your name', max_length=100)
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)
    sender=forms.EmailField()
    chore_completed=forms.BooleanField(required=False)

"""class EventForm(ModelForm):
    class Meta:
        model=Event
        fields=('name', 'event_date', 'venue', 'manager', 'description', 'attendess')
        labels={
           'name': '',
           'event_date': '',
           'venue': '',
           'manager': '',
           'description': '',
           'attendess': '', 
        }
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event name'}),
           'event_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Event Date'}),
           'venue': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Venue'}),
           'manager': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Manager'}),
           'description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Description'}),
           'attendess': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Attendess'}), 
        }"""