from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import View

from home.models import *

# Create your views here.

class Main(View):
    ctx = {
        "description":"",
        "keywords":"",
    }
    def get(self, request):
        return render(request=request, template_name="display/main.html", context=self.ctx)
