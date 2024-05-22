from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.detail import DetailView

from home.models import *
from django.apps import apps

app = apps.get_app_config('home')

# Create your views here.

class Main(LoginRequiredMixin, View):
    ctx = {
        "description":"",
        "keywords":"",
    }
    
    for model_name, model in app.models.items():
        ctx[model_name + "_list"] = model.objects.all()

    def get(self, request):
        return render(request=request, template_name="display/main.html", context=self.ctx)

