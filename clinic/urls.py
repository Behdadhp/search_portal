from django.urls import path
from clinic import views

app_name = 'clinic'

urlpatterns =[
    path('',views.ClinicListView.as_view(),name='clinic'),
    path('search',views.SearchResultView.as_view(),name='search'),
    path('details/<int:pk>',views.ClinicDetailsView.as_view(),name='details')
    ]
