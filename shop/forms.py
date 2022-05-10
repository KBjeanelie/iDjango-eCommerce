from django import forms
from django.contrib.auth.models import User
from django.forms import fields

from shop.models import Contact


class LoginForm(forms.ModelForm):
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
    model = User
    fields = ('username', 'email', 'password')

    widgets = {
        'username': forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "id": "InputUsername",
                "placeholder": "Enter Username",
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
