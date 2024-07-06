from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from . forms import *
# Create your views here.
def index(request):
    return render (request, 'index.html')

def contributors(request):
    return render (request, 'contributors.html')

def T_donor(request):
    if request.method == 'POST': 
        form = T_donorForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            return HttpResponse('form submitted successfully')  
        else:
            return render(request, 'T_donor.html', {'form': form})  
    else:
        form = T_donorForm()  
    return render(request, 'T_donor.html', {'form': form}) 


def P_donor(request):
    if request.method == 'POST': 
        form = P_donorForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            return HttpResponse('form submitted successfully')  
        else:
            return render(request, 'P_donor.html', {'form': form})  
    else:
        form = P_donorForm()  
    return render(request, 'P_donor.html', {'form': form}) 

def t_receiver(request):
    if request.method == 'POST':
        form = T_receiverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('t_receiver'))
        else:
            return render(request, 't_receiver.html', {'form': form})
    else:
        form = T_receiverForm()
        return render(request, 't_receiver.html', {'form': form})