from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'text', 'age', 'study', 'current_job', 'city']

        widgets = {
            'name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add name...'}),
            'text': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add your profile...'}),
            'age': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add your age...'}),
            'study': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add your studies level and university...'}),
            'current_job': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add your current job...'}),
            'city': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Add your current city...'}),
        }
