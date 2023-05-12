from modeltranslation.translator import translator, TranslationOptions
from .models import *


class MainAbilitiesTranslationOptions(TranslationOptions):
    fields = ('name',)
class EducationTranslationOptions(TranslationOptions):
    fields = ('title', 'text', 'university')
class ProfileTranslationOptions(TranslationOptions):
    fields = ('text','study', 'current_job', 'employment_status')
class ExperienceTranslationOptions(TranslationOptions):
    fields = ('location', 'position', 'text')
class RecentWorkTranslationOptions(TranslationOptions):
    fields = ('category', 'title')
class CertificatesTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
translator.register(MainAbilities, MainAbilitiesTranslationOptions)
translator.register(Education, EducationTranslationOptions)
translator.register(Profile, ProfileTranslationOptions)
translator.register(Experience, ExperienceTranslationOptions)
translator.register(RecentWork, RecentWorkTranslationOptions)
translator.register(Certificates, CertificatesTranslationOptions)
