from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from.forms import SignUpForm
from .models import Record

def home(request):
    records = Record.objects.all()

    #check if logging in
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

    #authenticate
        user = authenticate(request, username = username, password=password)
        if user is not None:
             login(request, user)
             messages.success(request, "you have been logged in")
             return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In, Please Try Again...")
            return redirect('home')
    else:
         return render(request, 'home.html', {'records': records})

def logout_user(request):
	logout(request)
	messages.success(request, "You Have Been Logged Out...")
	return redirect('home')

def register_user(request):
    form = SignUpForm(request.POST)
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,"you have successfully registered")
            return redirect('home')
        else:
             form = SignUpForm()
             return render(request, 'register.html',{'form':form})
    else:
        return render(request, 'register.html',{'form':form})


def customer_record(request, pk):
     if request.user.is_authenticated:
        #look up records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html',{'customer_record':customer_record})
     else:
          messages.success(request, "you must be logged in to view records")
          return redirect('home')