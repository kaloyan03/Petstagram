from datetime import datetime

from django.shortcuts import render
from django.urls import reverse_lazy

from django.views import generic as views

# Create your views here.
from petstagram.pets.forms import CreatePetForm, AddPetPhotoForm
from petstagram.pets.models import Pet, PetPhoto


class AddPetView(views.CreateView):
    template_name = 'pet_create.html'
    model = Pet
    form_class = CreatePetForm


class EditPetView(views.UpdateView):
    template_name = 'pet_edit.html'


class DeletePetView(views.DeleteView):
    template_name = 'pet_delete.html'

class ListPetsView(views.ListView):
    template_name = 'dashboard.html'
    model = Pet
    context_object_name = 'pets'

    def get_queryset(self):
        pets = Pet.objects.all()
        for pet in pets:
            pet.age = datetime.now().year - pet.date_of_birth.year

        return pets


class AddPetPhotoView(views.CreateView):
    template_name = 'photo_create.html'
    model = PetPhoto
    success_url = reverse_lazy('list pets view')
    form_class = AddPetPhotoForm



class EditPetPhotoView(views.UpdateView):
    template_name = 'photo_edit.html'

class DetailsPetView(views.TemplateView):
    template_name = 'photo_details.html'
    model = Pet

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet_id = self.kwargs['pk']
        pet = Pet.objects.get(id=pet_id)
        pet_photo = PetPhoto.objects.get(tagged_pets_id=pet.id)
        pet.photo = pet_photo.photo
        pet.description = pet_photo.description
        pet.age = datetime.now().year - pet.date_of_birth.year
        context['pet'] = pet



        return context



