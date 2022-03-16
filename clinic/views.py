from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from clinic import models
from django.db.models import Q
# Create your views here.



class ClinicListView(generic.ListView, LoginRequiredMixin):
    context_object_name = 'clinic_lists'
    queryset = models.Details.objects.all()
