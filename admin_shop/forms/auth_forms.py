from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    'id': 'email',
                    'class': 'form-control',
                    'title': 'please enter your email',
                    'name': 'email',
                    'placeholder': 'example@gmail.com',
                    'required': True

                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'type': 'password',
                    'id': 'password',
                    'class': 'form-control',
                    'title': 'please enter your email',
                    'name': 'password',
                    'placeholder': '********',
                    'required': True

                }
            )
        }


class AdminRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    'id': 'email',
                    'class': 'form-control',
                    'title': 'please enter your email',
                    'name': 'email',
                    'placeholder': 'example@gmail.com',
                    'required': True

                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'type': 'password',
                    'id': 'password',
                    'class': 'form-control',
                    'title': 'please enter your password',
                    'name': 'password',
                    'placeholder': '********',
                    'required': True

                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'type': 'first_name',
                    'id': 'first_name',
                    'class': 'form-control',
                    'title': 'please enter your first_name',
                    'name': 'first_name',
                    'placeholder': 'firstname',
                    'required': True

                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'type': 'last_name',
                    'id': 'last_name',
                    'class': 'form-control',
                    'title': 'please enter your lastname',
                    'name': 'lastname',
                    'placeholder': 'lastname',
                    'required': True

                }
            )
        }
