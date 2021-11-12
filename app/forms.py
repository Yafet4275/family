from django import forms
#from django.db.models.base import Model
from django.forms import fields, widgets, ModelForm
from .models import UserChore, Chore


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('start', 'Start'),
    ('done', 'Done'),
]


class SimpleForm(forms.Form):
    choices = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )


"""BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class SimpleForm(forms.Form):
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    favorite_colors = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=FAVORITE_COLORS_CHOICES,
    )"""


class UserChoreForm(forms.ModelForm):
    class Meta:
        model=UserChore
        fields=['name', 'lastName', 'gener']


class ChoreForm(forms.ModelForm):
    class Meta:
        model=Chore
        fields=['name', 'content', 'author', 'userchore', 'state']


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