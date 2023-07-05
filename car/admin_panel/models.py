from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import FileExtensionValidator
from user.models import User

# Create your models here.


# Brand Model
class Brand(models.Model):
    brand_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, unique=True, blank=True)

    def __str__(self):
        return self.brand_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand_name)
        return super().save(*args, **kwargs)


# Branch Model
class Branch(models.Model):
    branch_location = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    address = models.TextField(blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.branch_location

    def save(self, *args, **kwargs):
        self.slug = slugify(self.branch_location)
        return super().save(*args, **kwargs)


# Vehicle Model
class Vehicle(models.Model):
    transmission_choices = [
        ('manual', 'manual'),
        ('automatic', 'automatic')
    ]
    drive_choices = [
        ('2', '2'),
        ('4', '4')
    ]
    image1 = models.ImageField(validators=[FileExtensionValidator(
        ['png', 'jpg', 'jpeg'])], upload_to='vehicle_images')
    image2 = models.ImageField(validators=[FileExtensionValidator(
        ['png', 'jpg', 'jpeg'])], upload_to='vehicle_images', blank=True, null=True)
    image3 = models.ImageField(validators=[FileExtensionValidator(
        ['png', 'jpg', 'jpeg'])], upload_to='vehicle_images', blank=True, null=True)
    image4 = models.ImageField(validators=[FileExtensionValidator(
        ['png', 'jpg', 'jpeg'])], upload_to='vehicle_images', blank=True, null=True)
    image5 = models.ImageField(validators=[FileExtensionValidator(
        ['png', 'jpg', 'jpeg'])], upload_to='vehicle_images', blank=True, null=True)
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name='vehicles')
    branch = models.ForeignKey(
        Branch, on_delete=models.CASCADE, related_name='vehicles')
    vehicle_model = models.CharField(max_length=200)
    year = models.CharField(max_length=5)
    mileage = models.DecimalField(max_digits=10, decimal_places=4)
    vin = models.CharField(max_length=17)
    horsepower = models.IntegerField()
    transmission = models.CharField(
        max_length=10, choices=transmission_choices, default='manual')
    door = models.IntegerField()
    drive = models.CharField(max_length=20, choices=drive_choices, default='2')
    seat = models.IntegerField()
    color = models.CharField(max_length=20)
    price = models.IntegerField()
    stock = models.IntegerField()
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.brand} {self.vehicle_model}"

    def save(self, *args, **kwargs):
        self.slug = slugify(
            f"{self.brand}_{self.vehicle_model}_{self.branch.branch_location}")
        return super().save(*args, **kwargs)


# Vehicle Comment Model
class VehicleComment(models.Model):
    rating_choices = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    rating = models.CharField(max_length=10, choices=rating_choices)
    comment = models.TextField()
    should_show = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.comment} ~ {self.user.username}"


# New Car Model
class NewCar(models.Model):
    vehicle = models.OneToOneField(
        Vehicle, on_delete=models.CASCADE, related_name='new')

    def __str__(self):
        return f"{self.vehicle.brand.brand_name} {self.vehicle.vehicle_model}"


# About Us Model
class AboutUs(models.Model):
    about_text = models.CharField(max_length=300)
    service1 = models.CharField(max_length=70)
    service2 = models.CharField(max_length=70)
    service3 = models.CharField(max_length=70, blank=True, default="...")

    def __str__(self):
        return self.about_text
