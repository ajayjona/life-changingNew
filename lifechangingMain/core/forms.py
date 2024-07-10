from django import forms
from django.core.exceptions import ValidationError
from .models import *
from django.forms import ModelForm

class T_donorForm(forms.ModelForm):
    class Meta:
        model = T_donor
        fields = "__all__"

    def clean_td_name(self):
        td_name = self.cleaned_data.get('td_name')
        if not td_name:
            raise ValidationError("Name is required.")
        if not td_name.isalpha():
            raise ValidationError("Name should only contain alphabetic characters.")
        return td_name
    
    def clean_td_contact(self):
        td_contact = self.cleaned_data.get('td_contact')
        if td_contact is not None:
            if td_contact < 0:
                raise ValidationError("Contact number must be a positive integer.")
        return td_contact
    

class P_donorForm(forms.ModelForm):
    class Meta:
        model = P_donor
        fields = "__all__"


    def clean_D_name(self):
        D_name = self.cleaned_data.get('D_name')
        if not D_name:
            raise ValidationError("Name is required.")
        if not D_name.isalpha():
            raise ValidationError("Name should only contain alphabetic characters.")
        return D_name
    
    def clean_D_contact(self):
        D_contact = self.cleaned_data.get('D_contact')
        if D_contact is not None:
            if D_contact < 0:
                raise ValidationError("Contact number must be a positive integer.")
        return D_contact
   

class T_receiverForm(forms.ModelForm):
    class Meta:
        model = T_receiver
        fields = "__all__"
    
    def clean_tr_howtocontact(self):
        tr_howtocontact = self.cleaned_data.get('tr_howtocontact')
        if tr_howtocontact and not HowtoTrack.objects.filter(id=tr_howtocontact.id).exists():
            raise ValidationError("Selected contact method is invalid.")
        return tr_howtocontact

    def clean_tr_name(self):
        tr_name = self.cleaned_data.get('tr_name')
        if not tr_name:
            raise ValidationError("Name is required.")
        if not tr_name.isalpha():
            raise ValidationError("Name should only contain alphabetic characters.")
        return tr_name
    
    def clean_tr_contact(self):
        tr_contact = self.cleaned_data.get('tr_contact')
        if tr_contact is not None:
            if tr_contact < 0:
                raise ValidationError("Contact number must be a positive integer.")
        return tr_contact
    
    def clean_tr_photo_logo(self):
        tr_photo_logo = self.cleaned_data.get('tr_photo_logo')
        if tr_photo_logo and not tr_photo_logo.name.endswith(('.jpg', '.jpeg', '.png')):
            raise ValidationError("Photo logo must be a .jpg, .jpeg, or .png file.")
        return tr_photo_logo

    def clean(self):
        cleaned_data = super().clean()
        tr_name = cleaned_data.get("tr_name")
        tr_contact = cleaned_data.get("tr_contact")
        tr_location = cleaned_data.get("tr_location")

        # Example cross-field validation
        if tr_name and not tr_location:
            self.add_error('tr_location', "Location is required when name is provided.")
        
        return cleaned_data
    
class P_receiver(object):
    class Meta:
        model: P_receiver
        fields = "__all__"

    
    def clean_pr_howtocontact(self):
        pr_howtocontact = self.cleaned_data.get('pr_howtocontact')
        if pr_howtocontact and not HowtoTrack.objects.filter(id=pr_howtocontact.id).exists():
            raise ValidationError("Selected contact method is invalid.")
        return pr_howtocontact
    
    def clean_pr_name(self):
        pr_name = self.cleaned_data.get('pr_name')
        if not pr_name:
            raise ValidationError("Name is required.")
        if not pr_name.isalpha():
            raise ValidationError("Name should only contain alphabetic characters.")
        return pr_name
    
    def clean_pr_contact(self):
        pr_contact = self.cleaned_data.get('pr_contact')
        if pr_contact is not None:
            if pr_contact < 0:
                raise ValidationError("Contact number must be a positive integer.")
        return pr_contact
    
    def clean_pr_photo_logo(self):
        pr_photo_logo = self.cleaned_data.get('pr_photo_logo')
        if pr_photo_logo and not pr_photo_logo.name.endswith(('.jpg', '.jpeg', '.png')):
            raise ValidationError("Photo logo must be a .jpg, .jpeg, or .png file.")
        return pr_photo_logo
    
    def clean_pr_location(self):
        pr_location = self.cleaned_data.get('pr_location')
        if pr_location and not pr_location.isalpha():
            raise ValidationError("Location should only contain alphabetic characters.")
        return pr_location
    
    def clean_pr_description(self):
        pr_description = self.cleaned_data.get('pr_description')
        if pr_description and len(pr_description) > 250:
            raise ValidationError("Description should not exceed 600 characters.")
        return pr_description
    
    def clean(self):
        cleaned_data = super().clean()
        pr_name = cleaned_data.get("pr_name")
        pr_contact = cleaned_data.get("pr_contact")
        pr_location = cleaned_data.get("pr_location")
        pr_description = cleaned_data.get("pr_description")

        if pr_name and not pr_location:
            self.add_error('tr_location', "Location is required when name is provided.")
        
        return cleaned_data
    

    



