# from .models import Profile
from django import forms
from django.utils.translation import gettext_lazy as _

# class ProfileForm(forms.ModelForm):

#     class Meta:
#         model = Profile
#         fields = ['name', 'text', 'age', 'study', 'current_job', 'city']

#         widgets = {
#             'name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': _('Add name...')}),
#             'text': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': _('Add your profile...')}),
#             'age': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': _('Add your age...')}),
#             'study': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': _('Add your studies level and university...')}),
#             'current_job': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': _('Add your current job...')}),
#             'city': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': _('Add your current city...')}),
#         }


# class ContactForm(forms.Form):

#     class Meta:
#         fields = ['name', 'email', 'message']

#         widgets = {
#             'name': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': _('Add name...')}),
#             'email': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': _('Add your email...')}),
#             'message': forms.TextInput(attrs = {'class': 'form-control', 'placeholder': _('Add a few words...')}),

#         }