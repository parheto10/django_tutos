from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class InscriptionForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'last_name',
            'first_name',
            'email',
            'username',
            'password1',
            'password2',
        ]

    def save(self, commit=True):
        user = super(InscriptionForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "last_name",
            "first_name",
            "email",
            "password",
        ]
        exclude = [

        ]

