from django.db import models

# Create your models here.

# here we determine the category of uplift be it money, clothes etc
class P_category(models.Model):
    c_name = models.CharField(max_length=50)

    def _str_(self):
        return self.c_name

# this model represents a permanent donor and what is required of them
class P_donor(models.Model):
    GROUP_CHOICES =(
    ('select', 'Select'),
    ('money', 'Money'),
    ('clothes', 'Clothes'),
    ('food items', 'Food Items'),
    ('others', 'Others'),
    )
    D_item = models.CharField(max_length=50,choices= GROUP_CHOICES, null=True, blank=True)
    D_name = models.CharField(max_length=100, null = True, blank = True)
    D_item_name = models.CharField(max_length=100, null = True, blank = True)
    D_email = models.EmailField(max_length=100, null = True, blank = True)
    D_location = models.CharField(max_length=100, blank=True, null=True)
    D_verify = models.CharField( max_length=200,blank=True, null=True)
    D_photo_logo = models.ImageField(upload_to='images/', blank=True, null=True)
    D_contact = models.IntegerField( blank=True, null=True)
    D_description = models.CharField(max_length=600, blank=True, null=True)
    D_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.D_name

# this model represents a permanent reciever and what is required of them
class P_receiver(models.Model):
    PGROUP_CHOICES =(
    ('select', 'Select'),
    ('money', 'Money'),
    ('clothes', 'Clothes'),
    ('food items', 'Food Items'),
    ('others', 'Others'),
    )
    R_name = models.CharField(max_length=100, null = True, blank = True)
    R_item_name = models.CharField(max_length=100, null = True, blank = True)
    R_email = models.EmailField(max_length=100, null = True, blank = True)
    R_location = models.CharField(max_length=100, blank=True, null=True)
    R_reginfo = models.CharField( max_length=100,blank=True, null=True)
    R_item = models.CharField(max_length=50, choices= PGROUP_CHOICES, null=True, blank=True)
    R_photo_logo = models.ImageField(upload_to='images/', blank=True, null=True)
    R_contact = models.IntegerField( blank=True, null=True)
    R_description = models.CharField(max_length=600, blank=True, null=True)
    R_location = models.CharField(max_length=100, blank=True, null=True)
    R_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.R_name


# here you track your donations
class HowtoTrack(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True) 
    email = models.CharField(max_length=50, blank=True, null=True)
    telephone = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class T_donor(models.Model):
    CHOICES = (
        ('select', 'Select'),
        ('money', 'Money'),
        ('clothes', 'Clothes'),
        ('food items', 'Food Items'),
        ('others', 'Others'),
    )
    td_name = models.CharField(max_length=100)
    td_contact = models.IntegerField( blank=True, null=True)
    td_email = models.CharField(max_length=100, blank=True, null=True)
    td_location = models.CharField(max_length=100, blank=True, null=True)
    td_item = models.CharField(max_length=50, choices=CHOICES, null=True, blank=True)
    td_item_name = models.CharField(max_length=100,null=True, blank=True)
    td_photo_logo = models.ImageField(upload_to='images/',blank=True, null=True)
    td_description = models.TextField( blank=True, null=True)
    td_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.td_name

class T_receiver(models.Model):
    TCHOICES = (
        ('select', 'Select'),
        ('money', 'Money'),
        ('clothes', 'Clothes'),
        ('food items', 'Food Items'),
        ('others', 'Others'),
    )
    tr_name = models.CharField(max_length=100,blank=True, null=True)
    tr_email = models.CharField(max_length=100, blank=True, null=True)
    tr_contact = models.IntegerField( blank=True, null=True)
    tr_item = models.CharField(max_length=50, choices=TCHOICES, null=True, blank=True)
    tr_item_name = models.CharField(max_length=100,null=True, blank=True)
    tr_location = models.CharField(max_length=100, blank=True, null=True)
    tr_photo_logo = models.ImageField(upload_to='images/', blank=True, null=True)
    tr_description = models.TextField(max_length=600, blank=True, null=True)
    tr_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def _str_(self):
        return self.tr_name

# class Items(models.Model):
#     pass

# class Cloth(models.Model):
#     name = models.CharField(max_length=100, null=True, blank=True)
#     description = models.TextField(max_length=100, null=True, blank=True)
#     quantity = models.IntegerField(null=True, blank=True)
#     is_available = models.BooleanField(default=True)

#     def str(self):
#         return self.name

# class ClothImage(models.Model):
#     item = models.ForeignKey(Cloth, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images/')

#     def str(self):
#         return self.item.name + 'image'

# class clothRequest(models.Model):
#     requester = models.ForeignKey(Cloth, on_delete=models.CASCADE)
#     requester_name = models.CharField(max_length=100, null=True, blank=True)
#     item = models.ForeignKey(Cloth, on_delete=models.CASCADE)
#     request_message = models.TextField

#     def str(self):
#         return f"Request for {self.item.name} by {self.requester.username}"

## create forms for the models (frontend)


class Uplift(models.Model):
    user = models.ForeignKey(T_donor, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
