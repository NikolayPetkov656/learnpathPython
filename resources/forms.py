from django import forms

from .models import Resource


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ["title", "url", "resource_type", "description"]

        labels = {
            "title": "Resource title",
            "url": "Website address",
            "resource_type": "Resource type",
            "description": "Optional notes",
        }

        help_texts = {
            "title": "Use a descriptive title of at least 3 characters.",
            "url": "Include https:// or http:// in the address.",
            "resource_type": "Choose the format of this learning material.",
            "description": "Explain what makes this resource useful.",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "For example: Django Models Documentation",
                }
            ),
            "url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://docs.djangoproject.com/",
                }
            ),
            "resource_type": forms.Select(
                attrs={"class": "form-select"}
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Add a short explanation (optional).",
                }
            ),
        }

        error_messages = {
            "title": {
                "required": "Please enter a resource title.",
            },
            "url": {
                "required": "Please enter a website address.",
                "invalid": "Enter a valid address, such as https://example.com.",
            },
            "resource_type": {
                "required": "Please select a resource type.",
                "invalid_choice": "Choose one of the available resource types.",
            },
        }

    def clean_url(self):
        url = self.cleaned_data["url"]

        if not url.lower().startswith(("https://", "http://")):
            raise forms.ValidationError(
                "Use a web address starting with https:// or http://."
            )

        return url