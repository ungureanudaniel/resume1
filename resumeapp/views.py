from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.db.models import Count
from .forms import ProfileForm, ContactForm
from .models import Profile, MainAbilities, Education, Experience, Certificates, Skill, RecentWork



#--------------------------------------MAIN CV PAGE -------------------------------------------------
def home(request):
    about = Profile.objects.all()[:1]
    abilities = list(MainAbilities.objects.all())
    education = Education.objects.all()
    experience = Experience.objects.all()
    certificates = Certificates.objects.all()
    technical_skills = Skill.objects.filter(skill_type='technical', active='True')
    professional_skills = Skill.objects.filter(skill_type='professional', active='True')
    language_skills = Skill.objects.filter(skill_type='language')
    portfolio = RecentWork.objects.all()
    portfolio_count = RecentWork.objects.annotate(num_categories=Count('category'))
    print(portfolio_count)

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
            'technical_skills': technical_skills,
            'professional_skills': professional_skills,
            'language_skills': language_skills,
            'certificates': certificates,
            'experience': experience,
            'education': education,
            'portfolio': portfolio,
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
        # 'form': form,
        'technical_skills': technical_skills,
        'professional_skills': professional_skills,
        'language_skills': language_skills,
        'certificates': certificates,
        'experience': experience,
        'education': education,
        'portfolio': portfolio,
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

