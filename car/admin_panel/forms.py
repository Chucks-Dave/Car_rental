from django import forms

from main_site.models import FAQ
from .models import AboutUs, Branch, Brand, NewCar, Vehicle


# Brand Form
class BrandForm(forms.ModelForm):
    brand_name = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "col-12 form-control brand_name_input"}))

    class Meta:
        model = Brand
        fields = ('brand_name',)


# Branch Form
class BranchForm(forms.ModelForm):
    branch_location = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "col-12 form-control brand_name_input"}))
    phone_number = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "col-12 form-control brand_phone_number_input"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={"class": "col-12 form-control brand_email_input"}))
    address = forms.CharField(label='', widget=forms.Textarea(
        attrs={"class": "col-12 form-control brand_address_input"}))

    class Meta:
        model = Branch
        fields = ('branch_location', 'phone_number', 'email', 'address')


# Vehicle Form
class VehicleForm(forms.ModelForm):
    image1 = forms.FileField(
        label="", widget=forms.FileInput(attrs={"class": "d-none", "accept": "image/jpg, image/png, image/jpeg"}), required=True)
    image2 = forms.FileField(
        label="", widget=forms.FileInput(attrs={"class": "d-none", "accept": "image/jpg, image/png, image/jpeg", "required": False}), required=False)
    image3 = forms.FileField(
        label="", widget=forms.FileInput(attrs={"class": "d-none", "accept": "image/jpg, image/png, image/jpeg", "required": False}), required=False)
    image4 = forms.FileField(
        label="", widget=forms.FileInput(attrs={"class": "d-none", "accept": "image/jpg, image/png, image/jpeg", "required": False}), required=False)
    image5 = forms.FileField(
        label="", widget=forms.FileInput(attrs={"class": "d-none", "accept": "image/jpg, image/png, image/jpeg", "required": False}), required=False)
    brand = forms.Select()
    branch = forms.Select()
    vehicle_model = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control col-12 bg-transparent"}))
    year = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control col-12 bg-transparent"}))
    mileage = forms.DecimalField(label="", widget=forms.NumberInput(
        attrs={"class": "form-control col-12 bg-transparent"}))
    vin = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control col-12 bg-transparent"}))
    horsepower = forms.IntegerField(label="", widget=forms.NumberInput(
        attrs={"class": "form-control col-12 bg-transparent"}))
    transmission = forms.Select(
        attrs={"class": "form-select col-12 bg-transparent"})
    door = forms.IntegerField(label="", widget=forms.NumberInput(
        attrs={"class": "form-control col-12 bg-transparent"}))
    drive = forms.Select()
    seat = forms.IntegerField(label="", widget=forms.NumberInput(
        attrs={"class": "form-control col-12 bg-transparent"}))
    color = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control col-12 bg-transparent"}))
    price = forms.IntegerField(label="", widget=forms.NumberInput(
        attrs={"class": "form-control col bg-transparent"}))
    stock = forms.IntegerField(label="", widget=forms.NumberInput(
        attrs={"class": "form-control col-12 bg-transparent"}))

    class Meta:
        model = Vehicle
        fields = ('image1', 'image2', 'image3', 'image4', 'image5', 'brand', 'branch',
                  'vehicle_model', 'year', 'mileage', 'vin', 'horsepower', 'transmission', 'door', 'drive', 'seat', 'color', 'price', 'stock')


# New Car Form
class NewCarForm(forms.ModelForm):
    vehicle = forms.MultipleChoiceField(required=False, widget=forms.Select())

    class Meta:
        model = NewCar
        fields = ('vehicle',)


# About Us Form
class AboutUsForm(forms.ModelForm):
    about_text = forms.CharField(
        max_length=300, label="", widget=forms.Textarea(attrs={"maxlength": "300", "class": "form-control col-12", "rows": 3}))
    service1 = forms.CharField(max_length=70, label="", widget=forms.TextInput(
        attrs={"class": "form-control col-12"}))
    service2 = forms.CharField(max_length=70, label="", widget=forms.TextInput(
        attrs={"class": "form-control col-12"}))
    service3 = forms.CharField(max_length=70, label="", widget=forms.TextInput(
        attrs={"class": "form-control col-12"}), required=False)

    class Meta:
        model = AboutUs
        fields = ('about_text', 'service1', 'service2', 'service3')


# FAQ Form
class FaqForm(forms.ModelForm):
    reply = forms.CharField(label="", widget=forms.Textarea(attrs={
                            "class": "form-control col-12", "rows": 5, "placeholder": "Add a reply or answer to the question asked."}))

    class Meta:
        model = FAQ
        fields = ('reply',)
