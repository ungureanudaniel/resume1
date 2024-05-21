from django.contrib.sitemaps import Sitemap
# from .models import Skill, Certificates, RecentWork


class SkillSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    # def items(self):
    #     return Skill.objects.all()

    def location(self,obj):
        return '/%s' % (obj.skill_name)

class CertificatesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    # def items(self):
    #     return Certificates.objects.all()

    def location(self,obj):
        return '/%s' % (obj.title)

class RecentWorkSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'http'

    # def items(self):
    #     return RecentWork.objects.all()

    def location(self,obj):
        return '/%s' % (obj.title)
        
class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)
