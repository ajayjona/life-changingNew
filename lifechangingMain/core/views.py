from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *  
from .models import * 

# Create your views here.
def donor(request):
    if request.method == 'POST': 
        form = T_donorForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            return HttpResponse('form submitted successfully')  
        else:
            return render(request, 'donor.html', {'form': form})  
    else:
        form = T_donorForm()  
    return render(request, 'donor.html', {'form': form}) 
