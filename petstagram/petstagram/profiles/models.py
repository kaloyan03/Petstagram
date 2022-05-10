from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

UserModel = get_user_model()

# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do not show', 'Do not show'),
    )

    GENDER_MAX_LENGTH = max([len(x) for x, _ in GENDER_CHOICES])
    GENDER_MIN_LENGTH = min([len(x) for x, _ in GENDER_CHOICES])

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
        )
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures',
    )

    birth_day = models.DateTimeField()

    description = models.TextField()

    gender = models.CharField(
        choices=GENDER_CHOICES,
        max_length=GENDER_MAX_LENGTH,
        validators=(
            MinLengthValidator(GENDER_MIN_LENGTH),
        )

    )
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
    )