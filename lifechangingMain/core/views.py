from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    return render (request, 'index.html')

def contributors(request):
    return render (request, 'contributors.html')

def donor(request):
    return render (request, 'donor.html')
    # if request.method == 'POST': 
    #     form = T_donorForm(request.POST, request.FILES)  
    #     if form.is_valid():  
    #         form.save()  
    #         return HttpResponse('form submitted successfully')  
    #     else:
    #         return render(request, 'donor.html', {'form': form})  
    # else:
    #     form = T_donorForm()  
    # return render(request, 'donor.html', {'form': form}) 