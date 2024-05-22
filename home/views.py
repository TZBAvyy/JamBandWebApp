from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import View

from display.models import Event, Practice

# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    def get(self, request):
        ctx = {
            "description":"",
            "keywords":"",
            "event_list":Event.objects.all(),
            "practice_list":Practice.objects.all(),
        }
        return render(request=request, template_name='home/landing.html', context=ctx)

