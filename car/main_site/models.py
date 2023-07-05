from django.db import models

from admin_panel.models import Branch, Vehicle
from user.models import User

# Create your models here.


# Booking Model
class Booking(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="bookings")
    vehicle = models.ForeignKey(
        Vehicle, on_delete=models.CASCADE, related_name="bookings")
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="bookings")
    pick_up_location = models.CharField(
        'Pick up Location (optional)', max_length=500, blank=True)
    pick_up_date = models.DateTimeField()
    drop_off_date = models.DateTimeField()
    confirmed = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}: {self.vehicle.brand} {self.vehicle.vehicle_model} ~ {self.pick_up_date} - {self.drop_off_date}"


# Customer Review Model
class CustomerReview(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews")
    review = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.review} ~ {self.user.username}"


# Customer Query Model
class CustomerQuery(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=80)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.message} ~ {self.firstname} {self.lastname} {self.date}"


# FAQ Model
class FAQ(models.Model):
    query = models.ForeignKey(
        CustomerQuery, on_delete=models.CASCADE, related_name='faq')
    reply = models.TextField()

    def __str__(self):
        return f"{self.query.message} ~ {self.reply}"
