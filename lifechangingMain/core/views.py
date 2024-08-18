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
    t_contrib = T_donor.objects.all()
    p_contrib = P_donor.objects.all()
    return render (request, 'contributors.html',{'t_contrib':t_contrib ,'p_contrib':p_contrib} )

def friends(request):
    t_friend = T_receiver.objects.all()
    p_friend = P_receiver.objects.all()
    return render (request, 'friends.html',{'t_friend':t_friend ,'p_friend':p_friend} )

def t_donor(request):
    if request.method == 'POST': 
        form = T_donorForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
            return HttpResponseRedirect(reverse('contributors')) 
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
            return HttpResponseRedirect(reverse('contributors')) 
        else:
            return render(request, 'P_donor.html', {'groupform': groupform})  
    else:
        groupform = P_donorForm()  
    return render(request, 'P_donor.html', {'groupform': groupform}) 

def t_receiver(request):
    if request.method == 'POST':
        t_receiverform = T_receiverForm(request.POST, request.FILES)
        if t_receiverform.is_valid():
            t_receiverform.save()
            return HttpResponseRedirect(reverse('friends'))
        else:
            return render(request, 't_receiver.html', {'t_receiverform': t_receiverform})
    else:
        t_receiverform = T_receiverForm()
        return render(request, 't_receiver.html', {'t_receiverform': t_receiverform})

def p_receiver(request):
    if request.method == 'POST':

        p_receiverform = P_receiverForm(request.POST, request.FILES)
        if p_receiverform.is_valid():
            p_receiverform.save()
            return HttpResponseRedirect(reverse('friends'))

        else:
            return render(request, 'p_receiver.html', {'p_receiverform': p_receiverform})
    else:

        p_receiverform = P_receiverForm()
        return render(request, 'p_receiver.html', {'p_receiverform': p_receiverform})


def dashboard(request):
    if request.user.is_authenticated:
        donations = Donation.objects.filter(user=request.user)
        uplifts = Uplift.objects.filter(user=request.user)
    else:
        donations = []
        uplifts = []

    # Example: Placeholder for page views count or set a default value
    page_views = ...  # Logic to get page views count, or default to 0 if anonymous

    context = {
        "donations": donations,
        "uplifts": uplifts,
        "page_views": page_views,
    }
    return render(request, "dashboard.html", context)


def add_uplift(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")

        uplift = Uplift(user=request.user, title=title, description=description)
        uplift.save()
        return redirect("dashboard")

    return render(request, "add_uplift.html")
