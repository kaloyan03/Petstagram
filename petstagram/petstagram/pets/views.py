from django.shortcuts import render

from django.views import generic as views

# Create your views here.
class AddPetView(views.CreateView):
    pass


class EditPetView(views.UpdateView):
    pass


class DeletePetView(views.DeleteView):
    pass


class AddPetPhotoView(views.CreateView):
    pass


class EditPetPhotoView(views.UpdateView):
    pass

