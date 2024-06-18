from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from display.models import Member
from django.contrib.auth.models import User
from settings.models import UserProfile

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "settings/profile.html"
    fields = ['email']
    success_url = reverse_lazy('home:home')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["full_name"] = context["object"].get_full_name()

        member = UserProfile.objects.get(user=context["object"]).member
        if member:
            context["sections"] = member.sections.all()
            context["bands"] = member.bands.all()
            context["matric"] = context["object"].username[:-5] + "****" + context["object"].username[-1]
        else:
            context["sections"] = ""
            context["bands"] = ""
            context["matric"] = ""
        return context
    