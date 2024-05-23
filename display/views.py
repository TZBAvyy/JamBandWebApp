from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django import forms

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

#Event Model Views & Forms
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            "date": forms.widgets.SelectDateWidget(),
            "time": forms.TimeInput(attrs={'type': 'time'})
        }  

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('display:main')

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('display:main')

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    fields = '__all__'
    success_url = reverse_lazy('display:main')

#Practice Model Views & Forms
class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'
        widgets = {
            "date": forms.widgets.SelectDateWidget(),
            "startTime": forms.TimeInput(attrs={'type': 'time'}),
            "endTime": forms.TimeInput(attrs={'type': 'time'})
        }  

class PracticeCreate(LoginRequiredMixin, CreateView):
    model = Practice
    form_class = PracticeForm
    success_url = reverse_lazy('display:main')

class PracticeUpdate(LoginRequiredMixin, UpdateView):
    model = Practice
    form_class = PracticeForm
    success_url = reverse_lazy('display:main')

class PracticeDelete(LoginRequiredMixin, DeleteView):
    model = Practice
    fields = '__all__'
    success_url = reverse_lazy('display:main')

#Band Model Views & Forms
class BandCreate(LoginRequiredMixin, CreateView):
    model = Band
    field = "__all__"
    success_url = reverse_lazy('display:main')

#Band Model Views & Forms
class BandMemberCreate(LoginRequiredMixin, CreateView):
    model = BandMember
    field = "__all__"
    success_url = reverse_lazy('display:main')
