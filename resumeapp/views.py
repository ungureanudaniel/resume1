from django.shortcuts import render
from .models import Profile



# the main view
def home(request):
    profile = Profile.objects.all().order_by('-id')[:1]

    context = {
        'profile': profile,
    }
    return render(request, 'resume1/home.html', context)
