from django import forms

from petstagram.mixins import BootstrapFormMixin
from petstagram.profiles.models import Profile


class CreateProfileForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
