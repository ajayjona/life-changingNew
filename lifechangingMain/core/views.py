from django.shortcuts import render, redirect
from .forms import *  
from .models import * 

# Create your views here.
def donor(request):
    if request.method == 'POST': 
        form = T_donor(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('donor')  
        else:
            print("Form is not valid")  
    else:
        form = T_donorForm()  
    return render(request, 'donor.html', {'form': form}) 
