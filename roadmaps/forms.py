from django import forms

from .models import Roadmap


class RoadmapForm(forms.ModelForm):
    class Meta:
        model = Roadmap
        fields = ["title", "description", "difficulty"]

        labels = {
            "title": "Roadmap title",
            "description": "What will you learn?",
            "difficulty": "Difficulty level",
        }

        help_texts = {
            "title": "Use between 3 and 100 characters.",
            "description": "Explain the goal using at least 10 characters.",
            "difficulty": "Choose the level that best matches this roadmap.",
        }

        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "For example: Django Fundamentals",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Describe the skills this roadmap covers.",
                }
            ),
            "difficulty": forms.Select(
                attrs={"class": "form-select"}
            ),
        }

        error_messages = {
            "title": {
                "required": "Please enter a roadmap title.",
            },
            "description": {
                "required": "Please describe the learning goal.",
            },
            "difficulty": {
                "required": "Please choose a difficulty level.",
                "invalid_choice": "Choose one of the available difficulty levels.",
            },
        }