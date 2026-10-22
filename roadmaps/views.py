from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import RoadmapForm
from .models import Roadmap


class RoadmapListView(ListView):
    model = Roadmap
    template_name = "roadmaps/roadmap_list.html"
    context_object_name = "roadmaps"


class RoadmapDetailView(DetailView):
    model = Roadmap
    template_name = "roadmaps/roadmap_detail.html"
    context_object_name = "roadmap"


class RoadmapCreateView(CreateView):
    model = Roadmap
    form_class = RoadmapForm
    template_name = "roadmaps/roadmap_create.html"
    success_url = reverse_lazy("roadmaps:list")


class RoadmapUpdateView(UpdateView):
    model = Roadmap
    form_class = RoadmapForm
    template_name = "roadmaps/roadmap_edit.html"
    context_object_name = "roadmap"

    def get_success_url(self):
        return reverse(
            "roadmaps:detail",
            kwargs={"pk": self.object.pk},
        )


class RoadmapDeleteView(DeleteView):
    model = Roadmap
    template_name = "roadmaps/roadmap_confirm_delete.html"
    context_object_name = "roadmap"
    success_url = reverse_lazy("roadmaps:list")