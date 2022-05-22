from django import forms

from admin_shop.models import Marque


class MarqueCreationForm(forms.ModelForm):
    class Meta:
        model = Marque
        fields = ('label_marque',)

        widgets = {
            'label_marque': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Label",
                    "required": True
                }
            ),
        }


class MarqueUpdateForm(forms.ModelForm):
    class Meta:
        model = Marque
        fields = ('label_marque',)

        widgets = {
            'label_marque': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Label",
                    "required": True
                }
            ),
        }
