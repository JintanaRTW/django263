from django.urls import path
from django.http import HttpResponse
from ProfileApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('personal', views.personal, name='personal'),
    path('sale', views.sale, name='sale'),
    path('educational', views.educational, name='educational'),
    path('rolemodel', views.rolemodel, name='rolemodel'),
    path('interests', views.interests, name='interests'),
    path('showMyData', views.showMyData, name='showMyData'),
    path('listProduct', views.listProduct, name='listProduct'),
    path('inputProduct', views.inputProduct, name='inputProduct'),
]