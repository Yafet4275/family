from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from prueba.settings import LOGIN_URL
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import UserChoreForm, ChoreForm, SimpleForm
from .models import Chore, UserChore
#from django.core.mail import message, send_mail
from django.core.exceptions import ObjectDoesNotExist
import datetime
from django.db.models import Q
from django.core.paginator import Paginator

def login1(request):
    if request.method=='POST':
        #form=ChoreForm(request.POST)
        username = (request.POST['username'])
        password = (request.POST['password'])
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            now=datetime.datetime.now()
            usernameCap=username.capitalize()
            user=UserChore.objects.get(name=usernameCap)
            chores=Chore.objects.filter(userchore=user)
            return render(request, "app/user.html", {"user":user, "chores":chores, "now":now})
            # Redirect to a success page.
            #return redirect('home')
            #return render(request, "app/home1.html") 
            #return redirect('user')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    else:
        return render(request, 'app/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'login/login.html')

@login_required(login_url=LOGIN_URL)
def home(request):
    return render(request, 'login/home.html')

def home2(request):
    return render(request, 'app/index.html')

def calendar(request, year, month):
    name="John"
    a=calendar.month(2016, month)
    #month=month.capitalize()
    # Convert month from name to number
    #month_number=list(calendar.month).index(month)
    return render(request, 'app/calendar.html', {"name":name, "year":year, "month":month})

def startChore(request, chore_id):
    now=datetime.datetime.now()
    return render(request, 'app/home1.html', {'now':now})

"""def add_event(request):
    submitted=False
    if request.method=="POST":
        form=EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form=EventForm()
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'app/add_event.html', {'form':form, 'submitted':submitted})"""

def checkbox(request):
    form=SimpleForm()
    return render(request, 'app/home.html', {"form":form})

def yafetChore(request):
    now=datetime.datetime.now()
    user=UserChore.objects.get(id=5)
    chores=Chore.objects.filter(userchore=user)                           #Importing all fields in models.py
    queryset=request.GET.get("search")
    if queryset:
        chores=Chore.objects.filter(
            Q(name__icontains=queryset) | Q(content__icontains=queryset)        #It takes search word in the name or content ignoring the rest
        ).distinct()
    paginator=Paginator(chores, 5)                                              #Shows 2 products per page
    page=request.GET.get('page')                                                #Get what is the current page
    chores=paginator.get_page(page)                                             #Get list of product according with current page                
    return render(request, "app/user.html", {"user":user, "chores":chores, "now":now})                                               #Disting is to separate fron the one are iquals
    

@login_required(login_url=LOGIN_URL)
def home1(request):
    #chores=Chore.objects.all()              
    chores=Chore.objects.filter(state=True)
    queryset=request.GET.get("search")                                          #Getting information from GET method
    if queryset:
        chores=Chore.objects.filter(
            Q(name__icontains=queryset) | Q(content__icontains=queryset)        #It takes search word in the name or content ignoring the rest
        ).distinct()                                                            #Disting is to separate fron the one are iquals
    now=datetime.datetime.now()
    form=SimpleForm()
    paginator=Paginator(chores, 5)                                              #Shows 2 products per page
    page=request.GET.get('page')                                                #Get what is the current page
    chores=paginator.get_page(page)                                             #Get list of product according with current page
    return render(request, 'app/home1.html', {"chores":chores, "now":now, "form":form})

"""def add_event(request):
    submitted=False
    if request.method=="POST":
        form=EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')
    else:
        form=EventForm
        if 'submitted' in request.GET:
            submitted=True
    return render(request, 'app/add_event.html', {'form':form, 'submitted':submitted})"""   

def thanks(request):
    return render(request, 'app/thanks.html')

def user(request, user_id):
    now=datetime.datetime.now()
    user=UserChore.objects.get(id=user_id)
    print(user)
    chores=Chore.objects.filter(userchore=user)
    print(chores)                           #Importing all fields in models.py
    queryset=request.GET.get("search")
    if queryset:
        chores=Chore.objects.filter(
            Q(name__icontains=queryset) | Q(content__icontains=queryset)        #It takes search word in the name or content ignoring the rest
        ).distinct()
    paginator=Paginator(chores, 5)                                              #Shows 2 products per page
    page=request.GET.get('page')                                                #Get what is the current page
    chores=paginator.get_page(page)                                             #Get list of product according with current page                
    return render(request, "app/user.html", {"user":user, "chores":chores, "now":now})


def addChore(request):
    now=datetime.datetime.now()
    if request.method=='POST':
        #Create a form instance and populate it with data from the request:
        form=ChoreForm(request.POST)
        #Check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('home1')
            #Process the data in form.cleaned_data as required
            #subject=form.cleaned_data['subject']
            #message=form.cleaned_data['message']
            #sender=form.cleaned_data['sender']
            #chore_completed=form.cleaned_data['chore_completed']
            #recipients=['knowledgesoftware6@gmail.com']
            #if chore_completed:
            #    recipients.append(sender)
            #send_mail(subject, message, sender, recipients)
            #Redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    #if a GET (or any other method) We'll create a blank form
    else:
        form=ChoreForm()
    return render(request, 'app/AddChore.html', {'form':form, "now":now})
    

def addedChore(request):
    return render(request, "app/home1.html")

def chore(request, chore_id):
    now=datetime.datetime.now()   
    chores=Chore.objects.filter(id=chore_id)
    return render(request, "app/chore.html", {"chores":chores, "now":now})

def editChore(request, id):
    chore_form=None
    error=None
    try:
        chore=Chore.objects.get(id=id)
        if request.method=='GET':
            chore_form=ChoreForm(instance=chore) 
        else:
            chore_form=ChoreForm(request.POST, instance=chore)
            if chore_form.is_valid():
                chore_form.save()
            return redirect('home1')
    except ObjectDoesNotExist as e:
        error=e
    return render(request, 'app/edit_chore.html', {'form':chore_form, 'error':error})    

def removeChore(request, id):
    chore=Chore.objects.get(id=id)
    chore.state=False
    chore.save()
    #chore.delete()
    return redirect('home1')

"""def removeChore(request, id):
    chore=Chore.objects.get(id=id)
    if request.method=='POST':
        chore.state=False
        #chore.delete()
        chore.save()
        return redirect('home')
    return render(request, 'app/removeChore.html', {'chore':chore})"""

"""def CHECKBOXES(request):
    ms=['Start', 'Done']
    if request.method=='POST':
        tasks=request.POST.getlist('tasks')
        print(tasks)
        if tasks==['Start']:
            chores=Chore.objects.all()
            #chores.StartTask=             
            print('You seleted Start')
            #print(start)
        if tasks==['Done']:
            done=datetime.datetime.now()
            print('You seleted Done')
            print(done)
        if tasks==['Start', 'Done']:
            print('You seleted both and that is an invalid entry')
        if tasks==[]:
            print('Nothing was selected')
    return render(request, 'app/checkboxes.html')"""

def AddUser(request):
    now=datetime.datetime.now()
    #if this a POST request we need to process the form  data
    if request.method=='POST':
        #Create a form instance and populate it with data from the request:
        form=UserChoreForm(request.POST)
        #Check whether it's valid:
        if form.is_valid():
            form.save()
            return redirect('thanks')
            #Process the data in form.cleaned_data as required
            #subject=form.cleaned_data['subject']
            #message=form.cleaned_data['message']
            #sender=form.cleaned_data['sender']
            #chore_completed=form.cleaned_data['chore_completed']
            #recipients=['knowledgesoftware6@gmail.com']
            #if chore_completed:
            #    recipients.append(sender)
            #send_mail(subject, message, sender, recipients)
            #Redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    #if a GET (or any other method) We'll create a blank form
    else:
        form=UserChoreForm()
    
    return render(request, 'app/AddUser.html', {'form':form, 'now':now})


#def thanks(request):
#    return render()