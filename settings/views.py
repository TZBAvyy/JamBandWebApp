from typing import Any
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from display.models import Member, MemberSection
from django.contrib.auth.models import User
from settings.models import UserProfile

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "settings/profile.html"
    fields = ['email']

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["full_name"] = context["object"].get_full_name()

        if not self.request.user == context["object"]:
            raise PermissionDenied()

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
    
    
    
class AdminView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Member
    template_name = "settings/admin.html"

    def test_func(self) -> bool | None:
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["membersection_list"] = MemberSection.objects.all()
        return context
    