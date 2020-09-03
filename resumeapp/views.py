from django.shortcuts import render
from .forms import ProfileForm
from .models import Profile, MainAbilities, Education, Exchange, Experience



#--------------------------------------MAIN CV PAGE -------------------------------------------------
def home(request):
    about = Profile.objects.all()[:1]
    abilities = list(MainAbilities.objects.all())
    education = Education.objects.all()
    experience = Experience.objects.all()

    context = {
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
