from django.shortcuts import render
from constance import config
from .models import *
from django.http import Http404

def index(request):
    settings = config
    services = Service.objects.all()
    certs = Certification.objects.all()

    projects = Project.objects.all()
    social_media = SocialMedia.objects.all()
    skills = Skill.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
    "page_name": config.name,
    "services": services,
    "projects": projects,
    "social_media": social_media,
    "config": settings,
    "skills": skills,
    "testimonials": testimonials,
    "certefications":certs
    }
    return render(request, "portfolio/ui/pages/index.html", context)

def services(request):
    settings = config
    services = Service.objects.all()
    page_name = "Services"
    social_media = SocialMedia.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
    "page_name": page_name,
    "services": services,
    "social_media": social_media,
    "config": settings,
    "testimonials": testimonials
    }
    return render(request, "portfolio/ui/pages/services.html", context)

def projects(request):
    settings = config
    projects = Project.objects.all()
    page_name = "Projects"
    social_media = SocialMedia.objects.all()
    testimonials = Testimonial.objects.all()
    context = {
    "page_name": page_name,
    "projects": projects,
    "social_media": social_media,
    "config": settings,
    "testimonials": testimonials
    }
    return render(request, "portfolio/ui/pages/projects.html", context)

def service_detail(request, ServiceSlug):
    settings = config
    service = Service.objects.get(slug=ServiceSlug)
    questions = FAQ.objects.all().filter(service=service)
    other_services = Service.objects.exclude(slug=ServiceSlug)
    social_media = SocialMedia.objects.all()
    testimonials = Testimonial.objects.all()
    page_name = f"Service : {service.name}"
    context = {
    "service": service,
    "questions": questions,
    "other_services": other_services,
    "social_media": social_media,
    "config": settings,
    "testimonials": testimonials,
    "page_name": page_name
    }
    return render(request, "portfolio/ui/pages/service_detail.html", context)


def project_detail(request, ProjectSlug):
    settings = config
    project = Project.objects.get(slug=ProjectSlug)
    project_images = ProjectImage.objects.all().filter(project=project)
    next_project = Project.objects.filter(pk__gt=project.pk).order_by('pk').first()
    previous_project = Project.objects.filter(pk__lt=project.pk).order_by('-pk').first()
    social_media = SocialMedia.objects.all()
    testimonials = Testimonial.objects.all()
    page_name = f"Project : {project.name}"
    context = {
    "project": project,
    "project_images": project_images,
    "next_project": next_project,
    "previous_project": previous_project,
    "social_media": social_media,
    "config": settings,
    "testimonials": testimonials,
    "page_name": page_name
    }
    return render(request, "portfolio/ui/pages/project_detail.html", context)


def contact(request):
    if config.contact_info == True :
        settings = config
        social_media = SocialMedia.objects.all()
        testimonials = Testimonial.objects.all()
        page_name = "Contact page"
        context = {
        "social_media": social_media,
        "config": settings,
        "testimonials": testimonials,
        "page_name": page_name
        }
        return render(request, "portfolio/ui/pages/contact.html", context)
    else :
      raise Http404
