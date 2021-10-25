from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import myform
from . models import Chore, UserChore
from django.core.mail import message, send_mail
from datetime import datetime

def home(request):
    chores=Chore.objects.all()
    return render(request, 'app/home.html', {"chores":chores})

def thanks(request):
    return render(request, 'app/thanks.html')

def user(request, user_id):
    user=UserChore.objects.get(id=user_id) 
    chores=Chore.objects.filter(userchore=user)                           #Importing all fields in models.py
    return render(request, "app/user.html", {"user":user, "chores":chores})

def chore(request, chore_id):
    chores=Chore.objects.filter(id=chore_id)
    return render(request, "app/chore.html", {"chores":chores})

def CHECKBOXES(request):
    ms=['Start', 'Done']
    if request.method=='POST':
        tasks=request.POST.getlist('tasks')
        print(tasks)
        if tasks==['Start']:
            chores=Chore.objects.all()
            #chores.StartTask=             
            print('You seleted Start')
            print(start)
        if tasks==['Done']:
            done=datetime.datetime.now()
            print('You seleted Done')
            print(done)
        if tasks==['Start', 'Done']:
            print('You seleted both and that is an invalid entry')
        if tasks==[]:
            print('Nothing was selected')
    return render(request, 'app/checkboxes.html')

def get_name(request):
    #if this a POST request we need to process the form  data
    if request.method=='POST':
        #Create a form instance and populate it with data from the request:
        form=myform(request.POST)
        #Check whether it's valid:
        if form.is_valid():
            #Process the data in form.cleaned_data as required
            subject=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            sender=form.cleaned_data['sender']
            chore_completed=form.cleaned_data['chore_completed']
            recipients=['knowledgesoftware6@gmail.com']
            if chore_completed:
                recipients.append(sender)
            #send_mail(subject, message, sender, recipients)
            #Redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    #if a GET (or any other method) We'll create a blank form
    else:
        form=myform()
    
    return render(request, 'app/form.html', {'form':form})


#def thanks(request):
#    return render()