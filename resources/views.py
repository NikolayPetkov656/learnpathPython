from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ResourceForm
from .models import Resource


class ResourceListView(ListView):
    model = Resource
    template_name = "resources/resource_list.html"
    context_object_name = "resources"


class ResourceDetailView(DetailView):
    model = Resource
    template_name = "resources/resource_detail.html"
    context_object_name = "resource"

    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            "steps__roadmap"
        )


class ResourceCreateView(CreateView):
    model = Resource
    form_class = ResourceForm
    template_name = "resources/resource_create.html"
    success_url = reverse_lazy("resources:list")


class ResourceUpdateView(UpdateView):
    model = Resource
    form_class = ResourceForm
    template_name = "resources/resource_edit.html"
    context_object_name = "resource"

    def get_success_url(self):
        return reverse(
            "resources:detail",
            kwargs={"pk": self.object.pk},
        )


class ResourceDeleteView(DeleteView):
    model = Resource
    template_name = "resources/resource_confirm_delete.html"
    context_object_name = "resource"
    success_url = reverse_lazy("resources:list")