from django.shortcuts import render
from django.views.generic import TemplateView
import json
from datetime import datetime as dt

from display.models import Event, Practice

# Create your views here.

#Landing Page View (URL: '')
class Home(TemplateView):
    def get(self, request):
        events = []
        for event in Event.objects.all():
            if dt.combine(event.date,event.time)>dt.now():
                events.append(event)
        practices = Practice.objects.all()
        ctx = {
            "description":"Universe also known as Hall 1 Jam Band's Webpage",
            "keywords":"Universe, Hall 1, Jam Band, Hall 1 Jam Band, NTU, Nanyang Technological University,"+
            "NTU Jam Band, Oners, Universe Jam Band",
            "event_list":events, #Ref Event & Practice Models to show all values in landing page
        }
        if events or practices:
            events_json = []
            for event in events:
                events_json.append({
                    'title':event.name,
                    'start':event.date.strftime("%Y-%m-%d"),
                    'end':event.date.strftime("%Y-%m-%d")
                })
            for practice in practices:
                events_json.append({
                    'title':practice.band.name,
                    'start':practice.date.strftime("%Y-%m-%dT")+practice.startTime.strftime("%H:%M"),
                    'end':practice.date.strftime("%Y-%m-%dT")+practice.endTime.strftime("%H:%M")
                })
            ctx["events_json"] = json.dumps(events_json)
        else:
            ctx["events_json"] = json.dumps({})
        return render(request=request, template_name='home/landing.html', context=ctx)
    

