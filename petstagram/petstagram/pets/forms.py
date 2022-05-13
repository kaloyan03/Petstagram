from django import forms

from petstagram.mixins import BootstrapFormMixin
from petstagram.pets.models import Pet, PetPhoto


class CreatePetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'date_of_birth': forms.DateInput(format=('%d-%m-%Y'),
                                             attrs={
                                                    'type': 'date',
                                             })
        }


class AddPetPhotoForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = '__all__'
