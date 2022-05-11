from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    TYPE_CHOICES = (
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
        ('Bunny', 'Bunny'),
        ('Parrot', 'Parrot'),
        ('Fish', 'Fish'),
        ('Other', 'Other'),
    )

    TYPE_CHOICES_MAX_LENGTH = max([len(x) for x, _ in TYPE_CHOICES])
    TYPE_CHOICES_MIN_LENGTH = max([len(x) for x, _ in TYPE_CHOICES])

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        choices=TYPE_CHOICES,
        max_length=TYPE_CHOICES_MAX_LENGTH,
        validators=(
            MinLengthValidator(TYPE_CHOICES_MIN_LENGTH),
        )
    )

    date_of_birth = models.DateTimeField(

    )


class PetPhoto(models.Model):
    # TODO add max file size 5mb
    photo = models.ImageField(
        upload_to='pet_photos',
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(

    )

    publication_date = models.DateTimeField(
        auto_now_add=True,
    )


