from django import forms

from admin_shop.models import Category


class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('label_category', 'image')

        widgets = {
            'label_category': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Label",
                    "required": True
                }
            ),
            'image': forms.FileInput(
                attrs={
                    "type": "file",
                    "class": "form-control",
                }
            ),
        }


class CategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('label_category', 'image')

        widgets = {
            'label_category': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Label",
                    "required": True
                }
            ),
            'image': forms.FileInput(
                attrs={
                    "type": "file",
                    "class": "form-control",
                }
            ),
        }
