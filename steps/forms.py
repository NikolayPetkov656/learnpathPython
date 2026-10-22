from django import forms

from .models import Step


class StepForm(forms.ModelForm):
    class Meta:
        model = Step
        fields = [
            "roadmap",
            "title",
            "description",
            "position",
            "is_completed",
            "resources",
        ]

        labels = {
            "roadmap": "Parent roadmap",
            "title": "Step title",
            "description": "Learning instructions",
            "position": "Position in roadmap",
            "is_completed": "Mark as completed",
            "resources": "Learning resources",
        }

        help_texts = {
            "roadmap": "Choose the roadmap this step belongs to.",
            "title": "Use between 3 and 100 characters.",
            "description": "Explain what to study using at least 10 characters.",
            "position": "Use a number starting from 1.",
            "is_completed": "You can change this later.",
            "resources": "Select any useful resources. This field is optional.",
        }

        widgets = {
            "roadmap": forms.Select(
                attrs={"class": "form-select"}
            ),
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "For example: Understand Django Models",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Describe what this learning step involves.",
                }
            ),
            "position": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": 1,
                    "placeholder": "1",
                }
            ),
            "is_completed": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
            "resources": forms.CheckboxSelectMultiple(),
        }

        error_messages = {
            "roadmap": {
                "required": "Please choose a roadmap first.",
                "invalid_choice": "Choose an existing roadmap.",
            },
            "title": {
                "required": "Please enter a step title.",
            },
            "description": {
                "required": "Please explain what this step covers.",
            },
            "position": {
                "required": "Please enter the step position.",
                "invalid": "Enter a whole number starting from 1.",
                "min_value": "The minimum position must be at least 1.",
            },
            "resources": {
                "invalid_choice": "Choose resources from the available list.",
                "invalid_pk_value": "One of the selected resources is invalid.",
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["roadmap"].empty_label = "Choose a roadmap"

        if self.instance.pk:
            self.fields["roadmap"].disabled = True
            self.fields["roadmap"].help_text = (
                "The parent roadmap cannot be changed when editing a step."
            )