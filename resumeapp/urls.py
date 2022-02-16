from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .sitemaps import SkillSitemap, CertificatesSitemap, RecentWorkSitemap
from . import views

sitemaps = {
    'skills':SkillSitemap,
    'certificates':CertificatesSitemap,
    'portfolio':RecentWorkSitemap,
}

urlpatterns = [
    path('', views.home, name='index'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("robots.txt",TemplateView.as_view(template_name="resume1/robots.txt", content_type="text/plain")),
]
