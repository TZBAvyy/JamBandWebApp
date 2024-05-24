from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import View

from display.models import Event, Practice

# Create your views here.

#Landing Page View (URL: '')
class Home(TemplateView):
    def get(self, request):
        ctx = {
            "description":"Universe also known as Hall 1 Jam Band's Webpage",
            "keywords":"Universe, Hall 1, Jam Band, Hall 1 Jam Band, NTU, Nanyang Technological University,"+
            "NTU Jam Band, Oners, Universe Jam Band",
            "event_list":Event.objects.all(), #Ref Event & Practice Models to show all values in landing page
            "practice_list":Practice.objects.all(),
        }
        return render(request=request, template_name='home/landing.html', context=ctx)

