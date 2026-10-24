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

from django.db.models import Q
from django.views.generic import TemplateView

from resources.models import Resource
from steps.models import Step

from django.shortcuts import render


class RoadmapListView(ListView):
    model = Roadmap
    template_name = "roadmaps/roadmap_list.html"
    context_object_name = "roadmaps"

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.GET.get("q", "").strip()
        difficulty = self.request.GET.get("difficulty", "")
        sort = self.request.GET.get("sort", "title")

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search)
                | Q(description__icontains=search)
            )

        if difficulty in Roadmap.Difficulty.values:
            queryset = queryset.filter(difficulty=difficulty)

        ordering_options = {
            "title": ("title", "pk"),
            "newest": ("-created_at", "-pk"),
            "oldest": ("created_at", "pk"),
        }
        ordering = ordering_options.get(
            sort,
            ordering_options["title"],
        )

        return queryset.order_by(*ordering)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["search_query"] = self.request.GET.get("q", "").strip()
        context["selected_difficulty"] = self.request.GET.get(
            "difficulty", ""
        )
        context["selected_sort"] = self.request.GET.get("sort", "title")
        context["difficulty_choices"] = Roadmap.Difficulty.choices

        return context


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


class DashboardView(TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total_steps = Step.objects.count()
        completed_steps = Step.objects.filter(
            is_completed=True
        ).count()

        context["roadmap_count"] = Roadmap.objects.count()
        context["resource_count"] = Resource.objects.count()
        context["total_steps"] = total_steps
        context["completed_steps"] = completed_steps
        context["remaining_steps"] = total_steps - completed_steps
        context["overall_progress"] = (
            round(completed_steps / total_steps * 100)
            if total_steps
            else 0
        )
        context["recent_roadmaps"] = (
            Roadmap.objects.order_by("-created_at", "-pk")[:5]
        )
        context["pending_steps"] = (
            Step.objects.filter(is_completed=False)
            .select_related("roadmap")
            .order_by("roadmap__title", "position", "pk")[:5]
        )

        return context


def not_found_preview(request):
    return render(request, "404.html", status=404)