from django.contrib import admin
from .models import Profile, Education, Experience, Skill, Exchange, Certificates, MainAbilities
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'age', 'study', 'current_job', 'city')

class MainAbilitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'year', 'university')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'position', 'year', 'text',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'skill_type', 'skill_name')

class CertificatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('id', 'text')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(MainAbilities, MainAbilitiesAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Certificates, CertificatesAdmin)
admin.site.register(Exchange, ExchangeAdmin)
