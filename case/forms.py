from django import forms
from django.contrib.auth.models import User
from .models import Case

class CaseForm(forms.Form):
    # class Meta:
    #     model=Case
    #     fields="__all__"

    clinician=forms.ModelChoiceField(queryset=User.objects.all() )
    date=forms.DateField()
    name=forms.CharField()
    age=forms.FloatField()
    sex=forms.ChoiceField( choices=[
        ('M', 'Male'),
        ('F', 'Female'),
        ])
    phone=forms.CharField()
    father=forms.CharField()
    address=forms.CharField()
    sputum_afb_result=forms.ChoiceField( choices=[
        ('P', 'Positive'),
        ('N', 'Negative'),
        ('U', 'Unknown'),
    ])
    gxpert_result=forms.ChoiceField( choices=[
        ('N', 'MTB not detected'),
        ('I', 'Invalid'),
        ('T', 'MTB detected'),
        ('RR', 'Rif resistant'),
        ('TI', 'MTB detected & RR is invalid or no result'),
     ] )
    cxr_result=forms.ChoiceField( choices=[
        ('S', 'Suggestive of TB'),
        ('N', 'Not suggestive of TB'),
        ('D', 'Not Done')])
    other_investigation=forms.CharField(  )
    site_of_tb=forms.ChoiceField( choices=[
        ('P', 'Pulmonary TB'),
        ('E', 'Extra Pulmonary TB')])
    type_of_patient=forms.ChoiceField( choices=[
        ('N', 'New'),
        ('P', 'Previously Treated'),
        ('O', 'Other'),
        ('M', 'MDR-TB'),
    ])
    treatment_regimen=forms.ChoiceField( choices=[
        ('I', 'Initial'),
        ('R', 'Retreatment'),
        ('C', 'Childhood'),
        ('O', 'Other'),
       ])
    diabetes_mellitus=forms.ChoiceField( choices=[
        ('P', 'Positive'),
        ('N', 'Negative'),
        ('U', 'Unknown'),
       ])