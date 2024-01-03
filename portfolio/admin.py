from django.contrib import admin
from .models import *

class CertificationAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'institution', 'image')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

class ProjectImageAdmin(admin.TabularInline):
    model = ProjectImage

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'technologies', 'image')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    inlines = [
        ProjectImageAdmin,
    ]

class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'image', 'content', 'rate')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

class SkillAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'percent', 'icon')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']

class FAQAdmin(admin.TabularInline):
    model = FAQ

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'name', 'short_description', 'slug', 'icon')
    date_hierarchy = 'created_at'
    ordering = ['-created_at']
    inlines = [
        FAQAdmin,
    ]

admin.site.register(Certification, CertificationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Service, ServiceAdmin)

# Register your models here.
