from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import CaseForm


# Create your views here.
from .models import Case

class CaseList(LoginRequiredMixin, ListView):
    model = Case
    template_name = 'case_list.html'

class CaseView(LoginRequiredMixin, DetailView):
    model = Case
    template_name = 'case_detail.html'

class CaseCreate(LoginRequiredMixin, CreateView):
    template_name = 'case.html'
    model = Case
    fields=['name','date','age', 'sex','phone','father','address','sputum_afb_result','gxpert_result','cxr_result','other_investigation','site_of_tb', 'type_of_patient','treatment_regimen','diabetes_mellitus'  ]
    success_url = reverse_lazy('case_list')
    def form_valid(self, form):
        form.instance.clinician = self.request.user
        form.save()
        return super().form_valid(form)

class CaseUpdate(UpdateView):
    model = Case
    fields = ['name', 'pages']
    success_url = reverse_lazy('Case_list')

class CaseDelete(DeleteView):
    model = Case
    success_url = reverse_lazy('Case_list')