from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
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
        "description":"Test",
        "keywords":"",
    }

    def get(self, request):
        self.ctx["practice_list"] = Practice.objects.all().order_by('date','startTime')
        self.ctx["event_list"] = Event.objects.all().order_by('date','time')
        self.ctx["band_list"] = Band.objects.all()
        self.ctx["bandmember_list"] = BandMember.objects.all()
        return render(request=request, template_name="display/main.html", context=self.ctx)
    
class MemberView(LoginRequiredMixin, View):
    ctx = {
        "description":"",
        "keywords":"",
    }

    def get(self, request):
        self.ctx["section_list"] = Section.objects.all()
        self.ctx["membersection_list"] = MemberSection.objects.all().order_by('-proficiency')
        return render(request=request, template_name="display/members.html", context=self.ctx)

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
    fields = ['name']
    success_url = reverse_lazy('display:main')

    def form_valid(self, form: forms.BaseModelForm) -> HttpResponse:
        form.instance.event = get_object_or_404(Event, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
class BandUpdate(LoginRequiredMixin, UpdateView):
    model = Band
    fields = ['name']
    success_url = reverse_lazy('display:main')

class BandDelete(LoginRequiredMixin, DeleteView):
    model = Band
    fields = ['name']
    success_url = reverse_lazy('display:main')
