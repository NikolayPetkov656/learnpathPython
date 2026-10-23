from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)

from roadmaps.models import Roadmap

from .forms import StepForm
from .models import Step


class StepCreateView(CreateView):
    model = Step
    form_class = StepForm
    template_name = "steps/step_create.html"

    def get_initial(self):
        initial = super().get_initial()
        roadmap_id = self.request.GET.get("roadmap")

        if roadmap_id:
            roadmap = get_object_or_404(Roadmap, pk=roadmap_id)
            initial["roadmap"] = roadmap
            initial["position"] = (
                roadmap.steps.order_by("-position")
                .values_list("position", flat=True)
                .first()
                or 0
            ) + 1

        return initial

    def get_success_url(self):
        return reverse(
            "roadmaps:detail",
            kwargs={"pk": self.object.roadmap_id},
        )


class StepDetailView(DetailView):
    model = Step
    template_name = "steps/step_detail.html"
    context_object_name = "step"

    def get_queryset(self):
        return super().get_queryset().select_related(
            "roadmap"
        ).prefetch_related("resources")


class StepUpdateView(UpdateView):
    model = Step
    form_class = StepForm
    template_name = "steps/step_edit.html"
    context_object_name = "step"

    def get_success_url(self):
        return reverse(
            "steps:detail",
            kwargs={"pk": self.object.pk},
        )


class StepDeleteView(DeleteView):
    model = Step
    template_name = "steps/step_confirm_delete.html"
    context_object_name = "step"

    def get_success_url(self):
        return reverse(
            "roadmaps:detail",
            kwargs={"pk": self.object.roadmap_id},
        )