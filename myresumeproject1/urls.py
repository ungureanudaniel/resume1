
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static
from resumeapp.sitemaps import StaticViewSitemap
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from resumeapp.sitemaps import *
from django.conf.urls import handler404, handler500
sitemaps = {
    'static': StaticViewSitemap,
    'skillsitemap':SkillSitemap,
    'certificates':CertificatesSitemap,
    'recentwork':RecentWorkSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resumeapp.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path("robots.txt", TemplateView.as_view(template_name="services/robots.txt", content_type="text/plain"),),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = "resumeapp.views.page_not_found"
handler500 = "resumeapp.views.server_error"
