from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from clinic import models
from django.db.models import Q
from geopy.geocoders import GoogleV3
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

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)

        queryset_clinic_values = models.Details.objects.values().filter(id=self.kwargs['pk'])
        address = "{street}{house_number},{postal_code} {city}".format(street       =queryset_clinic_values[0]['street'],
                                                                       house_number =queryset_clinic_values[0]['house_number'],
                                                                       postal_code  =queryset_clinic_values[0]['postal_code'],
                                                                       city         =queryset_clinic_values[0]['city'])
        api_key = 'your_api'
        latitude_longitude = location(address,api_key)
        context['location'] =  "https://www.google.com/maps/embed/v1/place?key={api}&q={latitude},{longitude}".format(api=api_key,
                                                                                                                       latitude=latitude_longitude[0],
                                                                                                                       longitude=latitude_longitude[1])
        return context



def location(address,api_key):
    geolocator = GoogleV3(api_key)
    location = geolocator.geocode(address)

    return (location.latitude,location.longitude)
