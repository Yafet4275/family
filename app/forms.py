from django import forms

class myform(forms.Form):
    name=forms.CharField(label='Your name', max_length=100)
    subject=forms.CharField(max_length=100)
    message=forms.CharField(widget=forms.Textarea)
    sender=forms.EmailField()
    chore_completed=forms.BooleanField(required=False)
