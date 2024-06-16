from django.db import models

# Create your models here.

# here we determine the category of uplift be it money, clothes etc
class P_category(models.Model):
    c_name = models.CharField(max_length=50)

    def _str_(self):
        return self.c_name

# this model represents a permanent donor and what is required of them
class P_donor(models.Model):
    D_category = models.ForeignKey(P_category,on_delete=models.CASCADE, null=True, blank=True)
    D_name = models.CharField(max_length=100, null = True, blank = True)
    D_location = models.CharField(max_length=100, blank=True, null=True)
    D_regno = models.IntegerField( blank=True, null=True)
    D_photo_logo = models.ImageField( blank=True, null=True)
    D_contact = models.IntegerField( blank=True, null=True)
    D_description = models.CharField(max_length=600, blank=True, null=True)

    def _str_(self):
        return self.D_name

# this model represents a permanent reciever and what is required of them
class P_reciever(models.Model):
    R_category = models.ForeignKey(P_category,on_delete=models.CASCADE, null=True, blank=True)
    R_name = models.CharField(max_length=100, null = True, blank = True)
    R_location = models.CharField(max_length=100, blank=True, null=True)
    R_regno = models.IntegerField( blank=True, null=True)
    R_photo_logo = models.ImageField( blank=True, null=True)
    R_contact = models.IntegerField( blank=True, null=True)
    R_description = models.CharField(max_length=600, blank=True, null=True)
    R_location = models.CharField(max_length=100, blank=True, null=True)

    def _str_(self):
        return self.R_name


# here you track your donations 
class HowtoTrack(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True) 
    email = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)

    def _str_(self):
        return self.name

class T_donor(models.Model):
    td_howtocontact = models.ForeignKey(HowtoTrack,on_delete=models.CASCADE, null=True, blank=True)
    td_name = models.CharField(max_length=100)
    td_contact = models.IntegerField( blank=True, null=True)
    td_location = models.CharField(max_length=100, blank=True, null=True)
    td_photo_logo = models.ImageField( blank=True, null=True)

    def _str_(self):
        return self.td_name

class T_receiver(models.Model):
    tr_howtocontact = models.ForeignKey(HowtoTrack,on_delete=models.CASCADE, null=True, blank=True)
    tr_name = models.CharField(max_length=100)
    tr_contact = models.IntegerField( blank=True, null=True)
    tr_location = models.CharField(max_length=100, blank=True, null=True)
    tr_photo_logo = models.ImageField( blank=True, null=True)

    def _str_(self):
        return self.tr_name

class Items(models.Model):
    pass

class Cloth(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=100, null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    def str(self):
        return self.name

class ClothImage(models.Model):
    item = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def str(self):
        return self.item.name + 'image'

class clothRequest(models.Model):
    requester = models.ForeignKey(Cloth, on_delete=models.CASCADE, related_name='requester_requests')
    requester_name = models.CharField(max_length=100, null=True, blank=True)
    item = models.ForeignKey(Cloth, on_delete=models.CASCADE, related_name='item_requests')
    request_message = models.TextField()

    def __str__(self):
        return f"Request for {self.item.name} by {self.requester.username}"


## create forms for the models (frontend)