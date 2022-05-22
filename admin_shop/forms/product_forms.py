from django import forms

from admin_shop.models import Product


class ProductCreationForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('label', 'prices', 'description', 'size', 'quantity', 'marque',
                  'category', 'image1', 'image2', 'image3')

        widgets = {
            'label': forms.TextInput(
                attrs={
                    "type": "text",
                    "class": "form-control",
                    "placeholder": "Label",
                    "required": True
                }
            ),
            'description': forms.Textarea(
                attrs={
                    "rows": 5, "cols": 20,
                    'class': "form-control",
                    "placeholder": "Product description",
                }
            ),
            'prices': forms.NumberInput(
                attrs={
                    "type": "number",
                    "class": "form-control",
                    "required": True
                }
            ),
            'size': forms.Select(
                attrs={
                    "class": "form-control pro-edt-select form-control-primary",
                    "required": True
                }
            ),
            'quantity': forms.NumberInput(
                attrs={
                    "type": "number",
                    "class": "form-control",
                    "required": True
                }
            ),
            'marque': forms.Select(
                attrs={
                    "class": "form-control pro-edt-select form-control-primary",
                    "required": True
                }
            ),
            'category': forms.Select(
                attrs={
                    "class": "form-control",
                    "required": True
                }
            ),
            'image1': forms.FileInput(
                attrs={
                    "type": "file",
                    "class": "form-control",
                    "required": True
                }
            ),
            'image2': forms.FileInput(
                attrs={
                    "type": "file",
                    "class": "form-control",
                }
            ),
            'image3': forms.FileInput(
                attrs={
                    "type": "file",
                    "class": "form-control",
                }
            ),
        }
