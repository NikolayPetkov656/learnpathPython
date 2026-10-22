from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


class Step(models.Model):
    roadmap = models.ForeignKey(
        "roadmaps.Roadmap",
        on_delete=models.CASCADE,
        related_name="steps",
    )
    title = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(
                3,
                message="The step title must contain at least 3 characters.",
            )
        ],
    )
    description = models.TextField(
        validators=[
            MinLengthValidator(
                10,
                message="Describe this step using at least 10 characters.",
            )
        ],
    )
    position = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(
                1,
                message="The step position must be at least 1.",
            )
        ],
        help_text="Steps are displayed in this order, starting from 1.",
    )
    is_completed = models.BooleanField(default=False)

    resources = models.ManyToManyField(
        "resources.Resource",
        related_name="steps",
        blank=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["position", "pk"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(position__gte=1),
                name="step_position_at_least_one",
            ),
        ]

    def __str__(self):
        return self.title