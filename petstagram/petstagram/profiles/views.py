
from django.shortcuts import render
from django.views import generic as views

# Create your views here.
from petstagram.profiles.models import Profile


class ShowProfileView(views.DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'



class EditProfileView(views.UpdateView):
    pass


class DeleteProfileView(views.DeleteView):
    pass


