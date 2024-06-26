from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.views import View
from typing import Any
import json

from .models import *
from .forms import *
# Create your views here.

def createPracJson():
    practices = Practice.objects.all()
    if practices:
        practices_json = []
        for practice in practices:
            practices_json.append({
                'title':practice.band.name,
                'url': reverse('display:practice_update',args=[practice.id]),
                'start':practice.date.strftime("%Y-%m-%dT")+practice.startTime.strftime("%H:%M"),
                'end':practice.date.strftime("%Y-%m-%dT")+practice.endTime.strftime("%H:%M")
            })
        practices_json = json.dumps(practices_json)
    else:
        practices_json = json.dumps({})
    return practices_json

class Main(View):
    ctx = {
        "description":"Universe also known as Hall 1 Jam Band's Webpage",
        "keywords":"Universe, Hall 1, Jam Band, Hall 1 Jam Band, NTU, Nanyang Technological University",
    }

    def get(self, request):
        self.ctx["practice_list"] = Practice.objects.all()
        self.ctx["event_list"] = Event.objects.all()
        self.ctx["band_list"] = Band.objects.all()
        self.ctx["bandmember_list"] = BandMember.objects.all()
        self.ctx["practices_json"] = createPracJson()
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

#Practice Model Views
class PracticeCreate(LoginRequiredMixin, CreateView):
    model = Practice
    form_class = PracticeForm
    template_name = "display/form.html"
    success_url = reverse_lazy('display:main')

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["practices_json"] = createPracJson()
        return context

class PracticeUpdate(LoginRequiredMixin, UpdateView):
    model = Practice
    form_class = UpdatePracForm
    template_name = "display/form.html"
    success_url = reverse_lazy('display:main')
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["practices_json"] = createPracJson()
        return context

class PracticeDelete(LoginRequiredMixin, DeleteView):
    model = Practice
    fields = '__all__'
    template_name = "display/confirm_delete.html"
    success_url = reverse_lazy('display:main')

#THESE VIEWS ARE FOR SUPERUSER APP
#Event Model Views
class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "super/form.html"
    success_url = reverse_lazy('super:home')

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = "super/form.html"
    success_url = reverse_lazy('super:home')

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    fields = '__all__'
    template_name = "super/confirm_delete.html"
    success_url = reverse_lazy('super:home')

#Band Model Views & Forms
class BandCreate(LoginRequiredMixin, CreateView):
    model = Band
    form_class = BandForm
    template_name = "super/form.html"
    success_url = reverse_lazy('super:home')

    def form_valid(self, form: forms.BaseModelForm) -> HttpResponse:
        form.instance.event = get_object_or_404(Event, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
class BandUpdate(LoginRequiredMixin, UpdateView):
    model = Band
    fields = ['name']
    template_name = "super/form.html"
    success_url = reverse_lazy('super:home')

class BandDelete(LoginRequiredMixin, DeleteView):
    model = Band
    fields = ['name']
    template_name = "super/confirm_delete.html"
    success_url = reverse_lazy('super:home')

#Band Model Views
class BandMemberCreate(LoginRequiredMixin, CreateView):
    model = BandMember
    template_name = "super/form.html"
    form_class = BandMemberForm
    success_url = reverse_lazy('super:home')

    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super(BandMemberCreate, self).get_form_kwargs()
        kwargs['band_pk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form: forms.BaseModelForm) -> HttpResponse:
        form.instance.band = get_object_or_404(Band, pk=self.kwargs['pk'])
        return super().form_valid(form)

class BandMemberDelete(LoginRequiredMixin, DeleteView):
    model = BandMember
    template_name = "super/confirm_delete.html"
    success_url = reverse_lazy('super:home')

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        if queryset is None:
            queryset = self.get_queryset()
        band = self.kwargs["band_id"]
        member = self.kwargs["member_id"]
        obj = BandMember.objects.filter(band=band,member=member)
        return obj
