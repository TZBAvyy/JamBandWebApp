from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import View


# Create your views here.

class Home(LoginRequiredMixin, TemplateView):
    def get(self, request):
        ctx = {"description":"","keywords":""}
        return render(request=request, template_name='home/landing.html', context=ctx)

