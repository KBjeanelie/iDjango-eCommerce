from django import forms
from django.contrib.auth import get_user_model

from shop.models import Contact

User = get_user_model()


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'password')

        widgets = {
            'email': forms.EmailInput(
                attrs={
                    "type": "email",
                    "class": "form-control",
                    "id": "InputEmail",
                    "placeholder": "Enter Email",
                    "required": True
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    "type": "password",
                    "class": "form-control",
                    "id": "InputPassword",
                    "placeholder": "Enter Password",
                    "required": True
                }
            )
        }


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "InputFirstName",
                    "placeholder": "Enter firstname",
                    "required": True
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "InputLastName",
                    "placeholder": "Enter lastname",
                    "required": True
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    "type": "email",
                    "class": "form-control",
                    "id": "InputEmail",
                    "placeholder": "Enter Email",
                    "required": True
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    "type": "password",
                    "class": "form-control",
                    "id": "InputPassword",
                    "placeholder": "Enter Password",
                    "required": True
                }
            )
        }


class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("sender_name", "sender_email", "sender_subject", "sender_message")
        widgets = {
            'sender_name': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "name",
                    "name": "name",
                    "placeholder": "Your Name",
                    "required": True,
                    "data-error": "Please enter your name"
                }
            ),
            'sender_email': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "email",
                    "name": "email",
                    "placeholder": "Your Email",
                    "required": True,
                    "data-error": "Please enter your email"
                }
            ),
            'sender_subject': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "id": "subject",
                    "name": "subject",
                    "placeholder": "Your Subject",
                    "required": True,
                    "data-error": "Please enter your subject"
                }
            ),
            'sender_message': forms.Textarea(
                attrs={
                    "rows": "4",
                    "class": "form-control",
                    "id": "message",
                    "name": "name",
                    "placeholder": "Your Message",
                    "required": True,
                    "data-error": "Please enter your message"
                }
            ),
        }
