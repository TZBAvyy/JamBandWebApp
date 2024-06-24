from django import forms
from display.models import Event, Practice, Band
from datetime import datetime
from django.utils.timezone import localtime, make_aware, now

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            "date": forms.DateInput(attrs={'type':'date'}),
            "time": forms.TimeInput(attrs={'type': 'time'})
        }  

class PracticeForm(forms.ModelForm):
    band = forms.ModelChoiceField(queryset=Band.objects.filter(event__date__gt=datetime.now().date()))
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
