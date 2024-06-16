from . import views
from django.urls import path


urlpatterns = [
  path('donor/', views.donor, name='donor'),
  ]