from django import forms
from django.core.exceptions import ValidationError
from .models import T_receiver, HowtoTrack

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