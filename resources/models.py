from django.core.validators import MinLengthValidator
from django.db import models


class Resource(models.Model):
    class ResourceType(models.TextChoices):
        ARTICLE = "article", "Article"
        VIDEO = "video", "Video"
        DOCUMENTATION = "documentation", "Documentation"
        COURSE = "course", "Course"

    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(
                3,
                message="The resource title must contain at least 3 characters.",
            )
        ],
    )
    url = models.URLField(
        max_length=500,
        help_text="Enter a complete web address, including https://.",
        error_messages={
            "invalid": "Enter a valid web address, such as https://example.com.",
        },
    )
    resource_type = models.CharField(
        max_length=20,
        choices=ResourceType.choices,
        default=ResourceType.ARTICLE,
    )
    description = models.TextField(
        blank=True,
        help_text="Optionally explain why this resource is useful.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title", "pk"]

    def __str__(self):
        return self.title