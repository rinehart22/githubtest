from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Angel,Cod,Animal,Male,Female,Robot,Ch,Bike
from app.forms import SignupForm  
from django.contrib.auth import authenticate,login,logout  
from .forms import AngelForm 
from .models import Angel 
from django.contrib.auth.decorators import login_required






@login_required(login_url='login')

# Create your views here.
def begin(request):
    dynamicdata = Angel.objects.all()
    data = Cod.objects.all() 
    dat = Animal.objects.all()
    da = Male.objects.all()
    d = Female.objects.all()
    dy = Robot.objects.all()
    dyn = Ch.objects.all()
    db = Bike.objects.all()



    return render(request, 'begin.html', { 'x': dynamicdata ,'y': data, 'z': dat , 'w': da , 'v' : d, 'u':dy, 't': dyn , 's': db})

def delete(request, id):

    dynamicdata = Angel.objects.get(pk = id).delete()
    data = Cod.objects.get(pk=id).delete()
    dat = Animal.objects.get(pk = id).delete()
    da = Male.objects.get(pk = id).delete()
    d = Female.objects.get(pk = id).delete() 
    dy = Robot.objects.get(pk = id).delete()
    dyn = Ch.objects.get(pk = id).delete()
    db = Bike.objects.get(pk = id).delete()

    return redirect(request, 'delete.html', { 'x': dynamicdata, 'y': data, 'z': dat, 'w' : da, 'v': d, 'u': dy, 't': dyn, 's': db})

def read(request, id):
    dynamicdata=Angel.objects.get(pk = id)
    data = Cod.objects.get(pk = id)
    dat = Animal.objects.get(pk = id)
    da = Male.objects.get(pk = id)
    d = Female.objects.get(pk = id)
    dy = Robot.objects.get(pk = id)
    dyn = Ch.objects.get(pk = id)
    db = Bike.objects.get(pk = id)
    

    return render(request, 'read.html', {'x': dynamicdata ,'y': data, 'z': dat, 'w': da, 'v': d, 'u': dy, 't': dyn, 's': db}) 
def create(request):

    form = AngelForm() 
    if request.method == 'POST': 
        form = (request.POST)
        if form.is_valid():
            form.save() 
            return redirect('/app/begin') 
    return render(request, 'create.html', {'form': form})






def signup(request):

    form = SignupForm() 
    if request.method == 'POST':
        form = SignupForm(request.POST) 

        if form.is_valid():
            form.save() 
            

    return render(request, 'signup.html', {'form': form}) 

def loginn(request):

    if request.method == 'POST':

        username= request.POST.get('username')
        password= request.POST.get('password') 

        user =authenticate(request, username= username, password= password) 

        if user is not None:

            login(request,user) 

            return redirect('/app/begin')  

    return render(request, 'login.html') 

def logoutt(request): 
    logout(request)

    return redirect('/login') 
    
def base(request):
    return render(request, 'base.html')







    