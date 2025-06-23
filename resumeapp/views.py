from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Count
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils import timezone
from myresumeproject1 import settings
# from .forms import ProfileForm, ContactForm
from .models import Profile
# , MainAbilities, Education, Experience, Certificates, Skill, RecentWork


#----------------------AGE CALCULATION------------------------------
def calculate_age(born):
    today = timezone.now().date()  # current date with timezone awareness
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


#--------------------------------------MAIN CV PAGE -------------------------------------------------
def home(request, username=None):
    # AGE
    born = timezone.datetime(1986, 12, 18).date()
    age = calculate_age(born)
    # abilities = list(MainAbilities.objects.all())
    # education = Education.objects.all()
    # experience = Experience.objects.all()
    # skills = Skill.objects.filter(active='True')
    # portfolio_count = RecentWork.objects.annotate(num_categories=Count('category'))
    if request.method == "POST":
        subject = request.POST['name']
        email = request.POST['email']
        body = request.POST['message']

        email = EmailMessage(
            subject=subject,
            body=body,
            from_email=email,
            to=['ungureanu.daniel86@gmail.com'],
            
        )
        email.send(fail_silently=False)

        context = {
            # 'form': form,
            # 'technical_skills': technical_skills,
            # 'professional_skills': professional_skills,
            # 'language_skills': language_skills,
            # 'hobby_skills': hobby_skills,
            # 'skills': skills,
            # 'experience': experience,
            # 'education': education,
            # 'abilities': abilities,
            'message_name': subject,
            'message_email': email,
            'message': body,
        }
        return render(request, 'resume1/index.html', context)


    else:
    # return the page
        context = {
        'age': age,
        # 'skills': skills,
        # 'experience': experience,
        # 'education': education,
        # 'abilities': abilities,

        }
        return render(request, 'resume1/index.html', context)

