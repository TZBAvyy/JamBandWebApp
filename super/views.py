from typing import Any
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from display.models import Event, Band, MemberSection
# Create your views here.

class SuperView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Event
    template_name = "super/super.html"

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser

class BandDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Band
    template_name = "super/band_detail.html"

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["membersection_list"] = MemberSection.objects.all()
        return context