from django import forms
from django.db.models import Q
from .models import Event, Practice, Band, BandMember, Member
from datetime import datetime, time

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            "date": forms.DateInput(attrs={'type':'date'}),
            "time": forms.TimeInput(attrs={'type': 'time'})
        }  
    
class BandMemberForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        pk = kwargs.pop('band_pk')
        super().__init__(*args, **kwargs)
        self.fields['member'].queryset = Member.objects.filter(~Q(bands__id=pk))

    class Meta:
        model = BandMember
        fields = ['member']

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = ['name','members']
        widgets = {'members':forms.CheckboxSelectMultiple}

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

        if end==time(0,0):
            pass
        elif start > end: #start and end time validation
            raise forms.ValidationError("Start time cannot be later than end time!")
        
        date = cleaned_data.get('date')

        #Checks for if the current datetime > date + startTime to prevent booking of the room in the past
        dateNow = datetime.now().date()
        time8am = time(8,0)
        
        if dateNow>date:
            raise forms.ValidationError("Error, cannot book a practice in the past")
        
        if time8am>start:
            raise forms.ValidationError("Error, cannot book a practice before 8am")

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
    
class UpdatePracForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = '__all__'
        widgets = {
            "date": forms.DateInput(attrs={'type':'date'}),
            "startTime": forms.TimeInput(attrs={'type': 'time'}),
            "endTime": forms.TimeInput(attrs={'type': 'time'}),
            "band": forms.HiddenInput(),
        }  
    
    def clean(self): #Overrided clean method for additional validation
        cleaned_data = super(UpdatePracForm, self).clean()
        start = cleaned_data.get('startTime')
        end = cleaned_data.get('endTime')

        if end==time(0,0):
            pass
        elif start > end: #start and end time validation
            raise forms.ValidationError("Start time cannot be later than end time!")
        
        date = cleaned_data.get('date')

        #Checks for if the current datetime > date + startTime to prevent booking of the room in the past
        dateNow = datetime.now().date()
        time8am = time(8,0)
        
        if dateNow>date:
            raise forms.ValidationError("Error, cannot book a practice in the past")
        
        if time8am>start:
            raise forms.ValidationError("Error, cannot book a practice before 8am")

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
