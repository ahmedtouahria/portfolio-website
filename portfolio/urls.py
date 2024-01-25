from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('contact/', contact, name="Contact page"),
    path('services/', services, name="Services page"),
    path('projects/', projects, name="Projects page"),
    path('service/<slug:ServiceSlug>', service_detail, name="Service Detail"),
    path('project/<slug:ProjectSlug>', project_detail, name="Project Detail"),
    path('certefications/<slug:CertSlug>', certefication_details, name="certefication_details"),
    path('certefications/', certefications, name="certefications"),


]
