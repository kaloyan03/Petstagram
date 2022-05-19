
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from petstagram.profiles.forms import EditProfileForm

# Create your views here.
from petstagram.profiles.models import Profile


class ShowProfileView(views.DetailView):
    model = Profile
    template_name = 'profile_details.html'
    context_object_name = 'profile'



class EditProfileView(views.UpdateView):
    template_name = 'profile_edit.html'
    form_class = EditProfileForm
    queryset = Profile.objects.all()

    def get_success_url(self, **kwargs):
        return reverse_lazy('show profile view', kwargs = {'pk': self.object.id})




class DeleteProfileView(views.DeleteView):
    pass


