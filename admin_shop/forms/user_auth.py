from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import PasswordInput
from django.contrib.auth import get_user_model

from admin_shop.models import Profile

User = get_user_model()


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
       fields, plus a repeated password."""
    password1 = forms.CharField(label="Password", widget=PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValueError("Password does not match")

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'last_name', 'first_name', 'is_active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('Address', 'country', 'city', 'facebook_urls', 'twitter_urls', 'linkded_urls')
        widgets = {
            'Address': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Enter your address",
                }
            ),
            'country': forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            'city': forms.Select(
                attrs={
                    "class": "form-control",
                }
            ),
            'twitter_urls': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Enter your twitter's url",
                }
            ),
            'facebook_urls': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Enter your facebook's url",
                }
            ),
            'linkded_urls': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Enter your linkded's url",
                }
            ),

        }
