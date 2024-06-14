from django.forms import ModelForm
from .models import *

class T_donorForm(ModelForm):
    class Meta:
        model = T_donor
        fields = '__all__'  
