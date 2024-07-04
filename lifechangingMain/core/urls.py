from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contributors/', views.contributors, name='contributors'),
    path('donor/', views.donor, name='donor'),

    #t_receiver urls
    path('t_receiver/', views.t_receiver, name='t_receiver'),
    path('p_receiver/', views.p_receiver, name='p_receiver'),
]