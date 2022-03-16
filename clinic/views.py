from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from clinic import models
from django.db.models import Q
# Create your views here.



class ClinicListView(generic.ListView, LoginRequiredMixin):
    context_object_name = 'clinic_lists'
    queryset = models.Details.objects.all()

class SearchResultView (generic.TemplateView ,LoginRequiredMixin):
    template_name = 'clinic/search_result.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('s')
        clinic_lists = models.Details.objects.filter(
        Q(street=query) | Q(city=query) | Q(contract=query) | Q(specialist_group=query)
        )
        context["clinic_lists"] = clinic_lists

        return context

class ClinicDetailsView(generic.DetailView, LoginRequiredMixin):
    context_object_name = 'clinic_details'
    model = models.Details
    template_name = 'clinic/clinic_details.html'
