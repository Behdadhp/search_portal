from django.contrib import admin
from clinic.models import Doctors, Insurances, Details
# Register your models here.

class DoctorsAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','specialist_group','mail',)
    list_display_links = ('first_name','last_name',)

class DetailsAdmin(admin.ModelAdmin):
    list_display=('name','city','street', 'contract')
    list_display_links = ( 'city','name')


admin.site.register(Doctors,DoctorsAdmin)
admin.site.register(Insurances)
admin.site.register(Details,DetailsAdmin)
