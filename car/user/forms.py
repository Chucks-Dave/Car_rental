from django import forms

from .models import User


# Profile form
class ProfileForm(forms.ModelForm):
    profile_image = forms.FileField(
        label="", widget=forms.FileInput(attrs={"class": "form-control rounded-0", "accept": "image/png, image/jpg, image/jpeg", "required": False}), required=False)
    username = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control col ms-1 rounded-0 shadow-0"}))
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={"class": "form-control col ms-1 rounded-0 shadow-0"}))
    phone_number = forms.CharField(label="", widget=forms.TextInput(
        attrs={"class": "form-control col ms-1 rounded-0 shadow-0"}), required=False)

    class Meta:
        model = User
        fields = ('profile_image', 'username', 'email', 'phone_number')
