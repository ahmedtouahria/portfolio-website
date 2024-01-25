from django.shortcuts import render
from constance import config
from .models import *
from django.http import Http404

def index(request):
    services = Service.objects.all()
    certs = Certification.objects.all()
    projects = Project.objects.all()
    skills = Skill.objects.all()
    context = {
    "page_name": config.name,
    "services": services,
    "projects": projects,
    "skills": skills,
    "certefications":certs
    }
    return render(request, "portfolio/ui/pages/index.html", context)

def services(request):
    services = Service.objects.all()
    page_name = "Services"
    context = {
    "page_name": page_name,
    "services": services,
    }
    return render(request, "portfolio/ui/pages/services.html", context)

def projects(request):
    projects = Project.objects.all()
    page_name = "Projects"
    context = {
    "page_name": page_name,
    "projects": projects,
    }
    return render(request, "portfolio/ui/pages/projects.html", context)


def certefications(request):
    certs = Certification.objects.all()
    context = {
        "certefications":certs,
    }
    return render(request, "portfolio/ui/pages/certefications.html", context)

def certefication_details(request,CertSlug):
    certefication = Certification.objects.get(slug=CertSlug)
    page_name = f"Certification {certefication.name}"
    next_certefication = Certification.objects.all().order_by('-created_at').first()
    previous_certefication= Certification.objects.all().order_by('created_at').first()
    context = {
    "page_name": page_name,
    "certefication":certefication,
    "next_certefication":next_certefication,
    "previous_certefication":previous_certefication,


    }
    return render(request, "portfolio/ui/pages/certefication.html", context)


def service_detail(request, ServiceSlug):
    service = Service.objects.get(slug=ServiceSlug)
    questions = FAQ.objects.all().filter(service=service)
    other_services = Service.objects.exclude(slug=ServiceSlug)
    page_name = f"Service : {service.name}"
    context = {
    "service": service,
    "questions": questions,
    "other_services": other_services,
    "page_name": page_name
    }
    return render(request, "portfolio/ui/pages/service_detail.html", context)


def project_detail(request, ProjectSlug):
    project = Project.objects.get(slug=ProjectSlug)
    project_images = ProjectImage.objects.all().filter(project=project)
    next_project = Project.objects.filter(pk__gt=project.pk).order_by('pk').first()
    previous_project = Project.objects.filter(pk__lt=project.pk).order_by('-pk').first()
    page_name = f"Project : {project.name}"
    context = {
    "project": project,
    "project_images": project_images,
    "next_project": next_project,
    "previous_project": previous_project,
    "page_name": page_name
    }
    return render(request, "portfolio/ui/pages/project_detail.html", context)


def contact(request):
    if config.contact_info == True :
        page_name = "Contact page"
        context = {
        "page_name": page_name
        }
        return render(request, "portfolio/ui/pages/contact.html", context)
    else :
      raise Http404
