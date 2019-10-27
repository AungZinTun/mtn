from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
from django.conf import settings


class Case(models.Model):
    clinician=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )
    date=models.DateField()
    name=models.CharField(max_length=30)
    age=models.PositiveIntegerField()
    sex=models.CharField(max_length=1 , choices=(
        ('M', 'Male'),
        ('F', 'Female'),
        ))
    phone=models.CharField(max_length=10)
    father=models.CharField(max_length=30)
    address=models.CharField(max_length=100)
    sputum_afb_result=models.CharField(max_length=1, choices=(
        ('P', 'Positive'),
        ('N', 'Negative'),
        ('U', 'Unknown'),
        ))
    gxpert_result=models.CharField(max_length=2, choices=(
        ('N', 'MTB not detected'),
        ('I', 'Invalid'),
        ('T', 'MTB detected'),
        ('RR', 'Rif resistant'),
        ('TI', 'MTB detected & RR is invalid or no result'),
       
        ) )
    cxr_result=models.CharField(max_length=1, choices=(
        ('S', 'Suggestive of TB'),
        ('N', 'Not suggestive of TB'),
        ('D', 'Not Done')))
    other_investigation=models.CharField(max_length=100, null=True, blank=True )
    site_of_tb=models.CharField(max_length=1, choices=(
        ('P', 'Pulmonary TB'),
        ('E', 'Extra Pulmonary TB')))
    type_of_patient=models.CharField(max_length=1, choices=(
        ('N', 'New'),
        ('P', 'Previously Treated'),
        ('O', 'Other'),
        ('M', 'MDR-TB'),
        ))
    treatment_regimen=models.CharField(max_length=1, choices=(
        ('I', 'Initial'),
        ('R', 'Retreatment'),
        ('C', 'Childhood'),
        ('O', 'Other'),
        ), default="I")
    diabetes_mellitus=models.CharField(max_length=1, choices=(
        ('P', 'Positive'),
        ('N', 'Negative'),
        ('U', 'Unknown'),
        ))
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})

