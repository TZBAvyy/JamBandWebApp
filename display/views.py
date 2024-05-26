from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views import View
from django import forms
from datetime import datetime
from django.utils.timezone import localtime, make_aware, now

from display.models import *

# Create your views here.

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
            "date": forms.DateInput(attrs={'type':'date'}),
            "time": forms.TimeInput(attrs={'type': 'time'})
        }  

class EventCreate(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = "display/form.html"
    success_url = reverse_lazy('display:main')

class EventUpdate(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = "display/form.html"
    success_url = reverse_lazy('display:main')

class EventDelete(LoginRequiredMixin, DeleteView):
    model = Event
    fields = '__all__'
    template_name = "display/confirm_delete.html"
    success_url = reverse_lazy('display:main')

#Practice Model Views & Forms
class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'
        widgets = {
            "date": forms.DateInput(attrs={'type':'date'}),
            "startTime": forms.TimeInput(attrs={'type': 'time'}),
            "endTime": forms.TimeInput(attrs={'type': 'time'})
        }  
    
    def clean(self): #Overrided clean method for additional validation
        cleaned_data = super(PracticeForm, self).clean()
        start = cleaned_data.get('startTime')
        end = cleaned_data.get('endTime')

        if start > end: #start and end time validation
            raise forms.ValidationError(f"Start time cannot be later than end time! (No overnighters!)")
        
        date = cleaned_data.get('date')

        #Checks for if the current datetime > date + startTime to prevent booking of the room in the past
        datestartTime = make_aware(datetime.combine(date,start))
        datetimeNow = localtime(now())
        if datetimeNow>datestartTime:
            raise forms.ValidationError("Error, cannot book a practice in the past")

        conflicts = Practice.objects.filter(
                date=date,
                startTime__lt=end, #filter for any practices with startTime < endTime of this practice
                endTime__gt=start, #filter for any practices with endTime > startTime of this practice
            ).exclude(
                id=self.instance.id
            )
        if any(conflicts): #conflict validation 
            st = "Room is booked from "
            for i in conflicts:
                st += f"{i.startTime} to {i.endTime}, "
            raise forms.ValidationError(f"Conflict! {st}")
        return cleaned_data

class PracticeCreate(LoginRequiredMixin, CreateView):
    model = Practice
    form_class = PracticeForm
    template_name = "display/form.html"
    success_url = reverse_lazy('display:main')

class PracticeUpdate(LoginRequiredMixin, UpdateView):
    model = Practice
    form_class = PracticeForm
    template_name = "display/form.html"
    success_url = reverse_lazy('display:main')

class PracticeDelete(LoginRequiredMixin, DeleteView):
    model = Practice
    fields = '__all__'
    template_name = "display/confirm_delete.html"
    success_url = reverse_lazy('display:main')

#Band Model Views & Forms
class BandCreate(LoginRequiredMixin, CreateView):
    model = Band
    fields = ['name']
    template_name = "display/form.html"
    success_url = reverse_lazy('display:main')

    def form_valid(self, form: forms.BaseModelForm) -> HttpResponse:
        form.instance.event = get_object_or_404(Event, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
class BandUpdate(LoginRequiredMixin, UpdateView):
    model = Band
    fields = ['name']
    template_name = "display/form.html"
    success_url = reverse_lazy('display:main')

class BandDelete(LoginRequiredMixin, DeleteView):
    model = Band
    fields = ['name']
    template_name = "display/confirm_delete.html"
    success_url = reverse_lazy('display:main')

#Band Model Views & Forms
class BandMemberCreate(LoginRequiredMixin, CreateView):
    model = BandMember
    fields = ['member_section']
    template_name = "display/form.html"
    success_url = reverse_lazy('display:main')

    def form_valid(self, form: forms.BaseModelForm) -> HttpResponse:
        form.instance.band = get_object_or_404(Band, pk=self.kwargs['pk'])
        return super().form_valid(form)
    
class BandMemberUpdate(LoginRequiredMixin, UpdateView):
    model = BandMember
    fields = ['member_section']
    template_name = "display/form.html"
    success_url = reverse_lazy('display:main')

class BandMemberDelete(LoginRequiredMixin, DeleteView):
    model = BandMember
    fields = ['member_section']
    template_name = "display/confirm_delete.html"
    success_url = reverse_lazy('display:main')
