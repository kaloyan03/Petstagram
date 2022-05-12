from django.shortcuts import render
from django.views import generic as views

# Create your views here.
class ShowProfileView(views.TemplateView):
    pass

class EditProfileView(views.UpdateView):
    pass

