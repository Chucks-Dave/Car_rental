from django import forms

from admin_panel.models import VehicleComment
from .models import Booking, CustomerQuery, CustomerReview


# Vehicle Comment Form
class VehicleCommentForm(forms.ModelForm):
    comment = forms.CharField(label="", widget=forms.Textarea(
        attrs={"class": "col-12 form-control", "placeholder": "Type your comment...", "rows": 5}))

    class Meta:
        model = VehicleComment
        fields = ('comment',)


# Booking Form
class BookingForm(forms.ModelForm):
    pick_up_location = forms.CharField(label="Pick-Up Location (optional)", widget=forms.TextInput(
        attrs={"class": "form-control rounded-0 bg-light col-12", "placeholder": "(e.g. Oja Oba, Abule-Egba, Lagos.)"}), required=False)
    pick_up_date = forms.DateTimeField(label="Pick-Up Date", widget=forms.DateTimeInput(
        attrs={"type": "datetime-local", "class": "form-control rounded-0 bg-light col-12"}))
    drop_off_date = forms.DateTimeField(label="Drop-Off Date", widget=forms.DateTimeInput(
        attrs={"type": "datetime-local", "class": "form-control rounded-0 bg-light col-12"}))

    class Meta:
        model = Booking
        fields = ('pick_up_location', 'pick_up_date', 'drop_off_date')


# Customer Query Form
class CustomerQueryForm(forms.ModelForm):
    firstname = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control shadow-sm border-0 rounded-0 p-3 col-12", "placeholder": "First Name"}))
    lastname = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control shadow-sm border-0 rounded-0 p-3 col-12", "placeholder": "Last Name"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={
                             "class": "form-control shadow-sm border-0 rounded-0 p-3 col-12", "placeholder": "Email Address"}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={"class": "form-control shadow-sm border-0 rounded-0 p-3 col-12", "rows": 5, "placeholder": "Message"}), label="")

    class Meta:
        model = CustomerQuery
        fields = ('firstname', 'lastname', 'email', 'message')


# Customer Review Form
class CustomerReviewForm(forms.ModelForm):
    review = forms.CharField(label="", widget=forms.Textarea(attrs={
                             "class": "form-control shadow-sm border-0 rounded-0 p-3 col-12", "rows": 9, "placeholder": "Type here..."}))

    class Meta:
        model = CustomerReview
        fields = ('review',)
