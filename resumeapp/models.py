from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone

class MainAbilities(models.Model):
    id = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(max_length=200, default="forestry")

    def __str__(self):
        return self.name

#---------------------------PROFILE---------------------------------------
class Profile(models.Model):
    freelance_choices = (
        ('Free of Contract', 'Free of Contract'),
        ('Currently under contract', 'Currently under contract'),
)
    id = models.IntegerField(primary_key=True, default=1)
    # chap_title = models.CharField(max_length=200, default="")
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    # main_abilities = models.(MainAbilities, on_delete=models.CASCADE)
    text = models.TextField()
    age = models.IntegerField(default="5")
    study = models.CharField(max_length=200, default="")
    mail = models.EmailField(max_length=200, default="")
    current_job = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    website = models.CharField(max_length=200, default="")
    phone = models.IntegerField(default="0")
    employment_status = models.CharField(max_length=200, default="", choices=freelance_choices)

    def __str__(self):
        return self.text

#---------------------------EDUCATITON---------------------------------------
class Education(models.Model):
    title = models.CharField(max_length=200)
    university = models.CharField(max_length=300)
    year = models.TextField()
    text = models.TextField()

    def __str__(self):
        return self.title

#---------------------------EXPERIENCE---------------------------------------
class Experience(models.Model):
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200, default=" ")
    position = models.CharField(max_length=300)
    year = models.CharField(max_length=300)
    text = RichTextField()

    def __str__(self):
        return self.company

#---------------------------SKILLS---------------------------------------
class Skill(models.Model):
    skill_type = models.CharField(max_length=200, default="")
    skill_name = models.TextField()

    def __str__(self):
        return self.title

#---------------------------CONTACT---------------------------------------
class Contact(models.Model):
    title = models.CharField(max_length=200, default="Hi")
    text = models.TextField()

    def __str__(self):
        return self.title

#---------------------------CERTIFICATES---------------------------------------
class Certificates(models.Model):
    title = models.CharField(max_length=200, default="Hi")
    date = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

#---------------------------PROFILE---------------------------------------
class Exchange(models.Model):
    title = models.CharField(max_length=200, default="")
    text = models.TextField()

    def __str__(self):
        return self.title