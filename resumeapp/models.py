from django.db import models
# from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime  

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
    timestamp = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        # return reverse('post_detail', kwargs={'pk': self.pk})
        return reverse('home')

#---------------------------EDUCATITON---------------------------------------
class Education(models.Model):
    title = models.CharField(max_length=200)
    university = models.CharField(max_length=300)
    year = models.TextField()
    text = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.title

#---------------------------EXPERIENCE---------------------------------------
class Experience(models.Model):
    company = models.CharField(max_length=200)
    website = models.CharField(max_length=300)
    location = models.CharField(max_length=200, default=" ")
    position = models.CharField(max_length=300)
    year = models.CharField(max_length=300)
    text = models.TextField()
    timestamp = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.company

#---------------------------SKILLS---------------------------------------
class Skill(models.Model):
    skill_type_choice = (
        ('technical', 'technical'),
        ('professional', 'professional'),
        ('language', 'language')
    )
    skill_type = models.CharField(max_length=300, default="technical", choices=skill_type_choice)
    skill_name = models.CharField(max_length=200)
    percent = models.IntegerField()
    active = models.BooleanField(default='True')


    def __str__(self):
        return self.skill_name


#--------------------------RECENT WORK------------------------------------------
class RecentWork(models.Model):
    category = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

#---------------------------CONTACT---------------------------------------
# class Contact(models.Model):
#     name = models.CharField(max_length=200, default=" ")
#     email = models.EmailField(max_length=300)
#     message = models.TextField()
#
#     def __str__(self):
#         return self.name

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