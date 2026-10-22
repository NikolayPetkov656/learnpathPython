from django.core.validators import MinLengthValidator
from django.db import models


class Roadmap(models.Model):
    class Difficulty(models.TextChoices):
        BEGINNER = "beginner", "Beginner"
        INTERMEDIATE = "intermediate", "Intermediate"
        ADVANCED = "advanced", "Advanced"

    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(
                3,
                message="The roadmap title must contain at least 3 characters.",
            )
        ],
        help_text="Choose a clear title for your learning path.",
    )
    description = models.TextField(
        validators=[
            MinLengthValidator(
                10,
                message="Describe your roadmap using at least 10 characters.",
            )
        ],
    )
    difficulty = models.CharField(
        max_length=12,
        choices=Difficulty.choices,
        default=Difficulty.BEGINNER,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title", "pk"]

    def __str__(self):
        return self.title

    @property
    def total_steps(self):
        return self.steps.count()

    @property
    def completed_steps(self):
        return self.steps.filter(is_completed=True).count()

    @property
    def progress_percentage(self):
        total = self.total_steps

        if total == 0:
            return 0

        return round(self.completed_steps / total * 100)