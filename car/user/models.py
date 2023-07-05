from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser

# Create your models here.


# User model.
class User(AbstractUser):
    phone_number = models.CharField(max_length=20, blank=True, default='...')
    profile_image = models.ImageField(validators=[FileExtensionValidator(
        ['png', 'jpg', 'jpeg'])], upload_to='profile_images', blank=True)
