from django.urls import path
from clinic import views
from django.contrib.auth.decorators import login_required

app_name = 'clinic'

urlpatterns =[
    path('',login_required(views.ClinicListView.as_view()),name='clinic'),
    path('search',views.SearchResultView.as_view(),name='search'),
    path('details/<int:pk>',views.ClinicDetailsView.as_view(),name='details')
    ]
