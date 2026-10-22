from django.urls import path

from .views import (
    RoadmapCreateView,
    RoadmapDeleteView,
    RoadmapDetailView,
    RoadmapListView,
    RoadmapUpdateView,
)


app_name = "roadmaps"

urlpatterns = [
    path("", RoadmapListView.as_view(), name="list"),
    path("create/", RoadmapCreateView.as_view(), name="create"),
    path("<int:pk>/", RoadmapDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", RoadmapUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", RoadmapDeleteView.as_view(), name="delete"),
]