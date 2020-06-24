from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserLogin(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(max_length=64)


class UserRegister(forms.ModelForm):
    password = forms.CharField(max_length=64)
    password2 = forms.CharField(max_length=64)

    class Meta:
        model = User
        fields = ('username','email')

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("Inconsistent password input! Please try again")



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('phone','portrait','bio')