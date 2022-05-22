from django import forms

from admin_shop.models import Country


class CountryCreationForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name_country',)

        widgets = {
            'name_country': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Label",
                    "required": True
                }
            ),
        }


class CountryUpdateForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name_country',)

        widgets = {
            'name_country': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Label",
                    "required": True
                }
            ),
        }
