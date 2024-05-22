from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import View

from home.models import *

# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    def get(self, request):
        ctx = {
            "description":"",
            "keywords":""
        }
        return render(request=request, template_name='home/landing.html', context=ctx)

