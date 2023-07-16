from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

class Certification(models.Model):
    name = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    image = models.ImageField(upload_to='certification_images/')
    created_at = models.DateTimeField(auto_now=True)

class Project(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    content = RichTextField()
    video = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='project_principal_images/')
    date = models.DateTimeField(null=True, blank=True)
    client = models.CharField(max_length=255, null=True, blank=True)
    technologies = models.CharField(max_length=255, null=True, blank=True)
    live = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(unique=True, populate_from=('name'))

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='project_images/')
    created_at = models.DateTimeField(auto_now=True)

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    image = models.ImageField(upload_to='client_images/')
    content = models.TextField()
    rate = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

class Skill(models.Model):
    name = models.CharField(max_length=255)
    percent = models.PositiveIntegerField()
    color = models.CharField(max_length=255, blank=True, null=True)
    icon = models.ImageField(upload_to='skill_icons/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

class Service(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    content = RichTextField()
    icon = models.ImageField(upload_to='service_icons/')
    image = models.ImageField(upload_to='service_images/')
    video = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(unique=True, populate_from=('name'))


class FAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    question = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now=True)


class SocialMedia(models.Model):
    themify_icon = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
