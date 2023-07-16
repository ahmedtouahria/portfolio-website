from django.urls import path
from .views import index, service_detail, project_detail, services, projects, contact

urlpatterns = [
    path('', index, name="home"),
    path('contact/', contact, name="Contact page"),
    path('services/', services, name="Services page"),
    path('projects/', projects, name="Projects page"),
    path('service/<slug:ServiceSlug>', service_detail, name="Service Detail"),
    path('project/<slug:ProjectSlug>', project_detail, name="Project Detail")
]
