

from portfolio.models import SocialMedia, Testimonial


def global_scops(request):
    social_media = SocialMedia.objects.all()
    testimonials = Testimonial.objects.all()

    return {
            "social_media": social_media,
            "testimonials": testimonials,
    }