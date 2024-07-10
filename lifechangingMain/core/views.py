from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from . forms import *
# Create your views here.
def index(request):
    return render (request, 'index.html')

def about(request):
    return render (request, 'about.html')

def contributors(request):
    return render (request, 'contributors.html')
def t_donor(request):
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


def p_donor(request):
    if request.method == 'POST': 
        groupform = P_donorForm(request.POST, request.FILES)  
        if groupform.is_valid():  
            groupform.save()  
            return HttpResponse('form submitted successfully')  
        else:
            return render(request, 'P_donor.html', {'groupform': groupform})  
    else:
        groupform = P_donorForm()  
    return render(request, 'P_donor.html', {'groupform': groupform}) 

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


def p_receiver(request):
    if request.method == 'POST':
        form = P_receiverForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('p_receiver'))
        else:
            return render(request, 'p_receiver.html', {'form': form})
    else:
        form = P_receiverForm()
        return render(request, 'p_receiver.html', {'form': form})