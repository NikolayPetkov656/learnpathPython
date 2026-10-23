from django.urls import path

from .views import (
    ResourceCreateView,
    ResourceDeleteView,
    ResourceDetailView,
    ResourceListView,
    ResourceUpdateView,
)


app_name = "resources"

urlpatterns = [
    path("", ResourceListView.as_view(), name="list"),
    path("create/", ResourceCreateView.as_view(), name="create"),
    path("<int:pk>/", ResourceDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", ResourceUpdateView.as_view(), name="edit"),
    path("<int:pk>/delete/", ResourceDeleteView.as_view(), name="delete"),
]