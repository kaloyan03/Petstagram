from django import forms

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from petstagram.mixins import BootstrapFormMixin

UserModel = get_user_model()

class SignUpForm(BootstrapFormMixin, UserCreationForm):
    email = forms.EmailField(
        label="Email",
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        model = UserModel
        fields = ("email",)
        field_classes = {"email": UsernameField}
