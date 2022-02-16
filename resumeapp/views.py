from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Count
from .forms import ProfileForm, ContactForm
from .models import Profile, MainAbilities, Education, Experience, Certificates, Skill, RecentWork



#--------------------------------------MAIN CV PAGE -------------------------------------------------
def home(request):
    about = Profile.objects.filter(status='active')
    abilities = list(MainAbilities.objects.all())
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.filter(active='True')
    # portfolio_count = RecentWork.objects.annotate(num_categories=Count('category'))
    if request.method == "POST":
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        send_mail(
            message_name,  # name of sender
            message,  # text
            message_email,  # email
            ['danielungureanu531@gmail.com'],  # to email
            fail_silently=False,
        )

        context = {
            # 'form': form,
            # 'technical_skills': technical_skills,
            # 'professional_skills': professional_skills,
            # 'language_skills': language_skills,
            # 'hobby_skills': hobby_skills,
            'skills': skills,
            'experience': experience,
            'education': education,
            'abilities': abilities,
            'about': about,
            'message_name': message_name,
            'message_email': message_email,
            'message': message,
        }
        return render(request, 'resume1/index.html', context)


    else:
    # return the page
        context = {
        'skills': skills,
        'experience': experience,
        'education': education,
        'abilities': abilities,
        'about': about,

        }
        return render(request, 'resume1/index.html', context)

#--------------------------------------ADD PROFILE PAGE -------------------------------------------------
def add_profile(request):
    form = ProfileForm(request.POST or None)

    if form.is_valid():
        form.save()
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'resume1/add_profile.html', context)
