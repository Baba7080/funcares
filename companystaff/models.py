from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

CHOICES_STATUS = [
    ('Active', 'Active'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
    ('Rejected', 'Rejected')
]

# Create your models here.
class Loan(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=100)
    clientName = models.CharField(max_length=100)
    PAN = models.CharField(max_length=16)
    number = models.IntegerField()
    amount = models.IntegerField()
    email = models.EmailField(blank=True)
    creation = models.DateField(max_length=8,null=False)

    status = models.CharField(
        max_length=50,
        choices=CHOICES_STATUS,
        default='Active',
        verbose_name='Status'
    )


    def __str__(self):
        return self.clientName
    
class Insurance(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=100)
    clientName = models.CharField(max_length=100)
    PAN = models.CharField(max_length=16)
    number = models.IntegerField()
    amount = models.IntegerField()
    email = models.EmailField(blank=True)
    creation = models.DateField(max_length=8,null=True)

    status = models.CharField(
        max_length=50,
        choices=CHOICES_STATUS,
        default='Active',
        verbose_name='Status'
    )
    def __str__(self):
        return self.clientName
    


class Mutual_Fund(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=100)
    clientName = models.CharField(max_length=100)
    PAN = models.CharField(max_length=16)
    number = models.IntegerField()
    amount = models.IntegerField()
    email = models.EmailField(blank=True)
    creation = models.DateField(max_length=8,null=True)
    status = models.CharField(
        max_length=50,
        choices=CHOICES_STATUS,
        default='Active',
        verbose_name='Status'
    )

    def __str__(self):
        return self.clientName
    
class Demat_Account(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    type = models.CharField(max_length=100)
    clientName = models.CharField(max_length=100)
    PAN = models.CharField(max_length=16)
    number = models.IntegerField()
    amount = models.IntegerField()
    email = models.EmailField(blank=True)
    creation = models.DateField(max_length=8,null=True)
    status = models.CharField(
        max_length=50,
        choices=CHOICES_STATUS,
        default='Active',
        verbose_name='Status'
    )

    def __str__(self):
        return self.clientName