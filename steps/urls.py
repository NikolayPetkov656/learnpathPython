from django.urls import path

from .views import (
    StepCreateView,
    StepDeleteView,
    StepDetailView,
    StepUpdateView,
)


app_name = "steps"

urlpatterns = [
    path("create/", StepCreateView.as_view(), name="create"),
    path("<int:pk>/", StepDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", StepUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", StepDeleteView.as_view(), name="delete"),
]