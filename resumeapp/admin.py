from django.contrib import admin
from .models import Profile
# , Education, Experience, Skill, Exchange, Certificates, MainAbilities, RecentWork, CvFile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'age', 'study', 'current_job', 'city', 'status')

# class MainAbilitiesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name')

# class EducationAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'text', 'year', 'university')

# class ExperienceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'company', 'website', 'position', 'year', 'text',)

# class SkillAdmin(admin.ModelAdmin):
#     list_display = ('id', 'skill_type', 'skill_name', 'percent', 'active')

# class CertificatesAdmin(admin.ModelAdmin):
#     list_display = ('id', 'text')

# class ExchangeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'text')

# class RecentWorkAdmin(admin.ModelAdmin):
#     list_display = ('id', 'category', 'title', 'image')

# class CvFileAdmin(admin.ModelAdmin):
#     list_display = ('timestamp', 'file')

admin.site.register(Profile, ProfileAdmin)
# admin.site.register(RecentWork, RecentWorkAdmin)
# admin.site.register(MainAbilities, MainAbilitiesAdmin)
# admin.site.register(Education, EducationAdmin)
# admin.site.register(Experience, ExperienceAdmin)
# admin.site.register(Skill, SkillAdmin)
# admin.site.register(Certificates, CertificatesAdmin)
# admin.site.register(Exchange, ExchangeAdmin)
# admin.site.register(CvFile, CvFileAdmin)
