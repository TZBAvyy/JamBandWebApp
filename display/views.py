from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.detail import DetailView

from display.models import *
from django.apps import apps

app = apps.get_app_config('display')

# Create your views here.

class Main(LoginRequiredMixin, View):
    ctx = {
        "description":"",
        "keywords":"",
    }

    def get(self, request):
        for model_name, model in app.models.items():
            self.ctx[model_name + "_list"] = model.objects.all()
        return render(request=request, template_name="display/main.html", context=self.ctx)
    

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('display:main')

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('display:main')

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('display:main')

