from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    Male = "Mal"
    Female = "Fem"
    gender_choice = [
        (Male, "Male"),
        (Female, "Female"),
    ]
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=gender_choice) 

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'username',
                  'email',
                  'gender',
                  'password1',
                  'password2',
                  ]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].help_text = None


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username',]
        help_texts = {
            "username": None,
        }
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "required": "false"})
        }


class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['avatar',]
        help_texts = {
            "username": None,
        }
        widgets = {
            "avatar": forms.FileInput(attrs={"class": "form-control", "required": "false"})
        }


