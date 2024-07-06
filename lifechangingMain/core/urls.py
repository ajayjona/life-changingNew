from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contributors/', views.contributors, name='contributors'),
    path('T_donor/', views.T_donor, name='T_donor'),
    path('P_donor/', views.P_donor, name='P_donor'),

    #t_receiver urls
    path('t_receiver/', views.t_receiver, name='t_receiver'),
]