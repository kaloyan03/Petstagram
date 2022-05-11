from django.contrib.auth import views as auth_views, authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.auth_app.forms import SignUpForm, SignInForm
from petstagram.profiles.forms import CreateProfileForm


class SignUpView(views.TemplateView):
    template_name = 'profile_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sign_up_form'] = SignUpForm()
        context['profile_form'] = CreateProfileForm()

        return context

    def post(self, request, *args, **kwargs):
        profile_form = CreateProfileForm(request.POST, request.FILES)
        sign_up_form = SignUpForm(request.POST)

        if profile_form.is_valid() and sign_up_form.is_valid():
            user = sign_up_form.save()
            profile = profile_form.save(commit=False)

            profile.user = user

            profile.save()

            return redirect('home page')

        return render(request, 'profile_create.html', context={'profile_form': profile_form, 'sign_up_form': sign_up_form})


class SignInView(auth_views.LoginView):
    template_name = 'login_page.html'
    form_class = SignInForm
    next_page = reverse_lazy('home page')


