from django.shortcuts import render



# the main view
def home(request):
    return render(request, 'resume1/home.html', {})
