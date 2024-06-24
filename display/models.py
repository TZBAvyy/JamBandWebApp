from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# ALL MODELS FOLLOW THIS ERD: https://drawsql.app/teams/solo-196/diagrams/jamband

class Section(models.Model):
    instrument = models.CharField(
            max_length=50, 
            help_text='Enter a section (e.g. Bass)',
            validators=[MinLengthValidator(2, "Section instrument must be greater than 1 character")]
    )

    def __str__(self):
        """String for representing the Sections object."""
        return self.instrument
    
class Member(models.Model):
    name = models.CharField(
            max_length=50, 
            help_text='Enter a member\'s full name (e.g. Avi)',
            validators=[MinLengthValidator(2, "Member name must be greater than 1 character")]
    )
    sections = models.ManyToManyField('Section',through='MemberSection', related_name='players')

    def __str__(self):
        """String for representing the Members object."""
        return self.name
    
class MemberSection(models.Model):
    class Proficiency(models.IntegerChoices):
        LEARNING = 1
        CAN_PLAY = 2
    
    proficiency = models.IntegerField(choices=Proficiency)

    section = models.ForeignKey('Section', on_delete=models.CASCADE, null=False)
    member = models.ForeignKey('Member', on_delete=models.CASCADE, null=False)

    def __str__(self):
        """String for representing the MemberSections object."""
        if self.proficiency==1:
            s = " (L)"
        else:
            s = ""
        return f"{self.member} ({self.section}{s})"

class Event(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Event name must be greater than 1 character")]
    )
    date = models.DateField()
    
    time = models.TimeField()

    class Meta:
        ordering = ['-date','-time']

    # Shows up in the admin list
    def __str__(self):
        """String for representing the Events object."""
        return self.name
    
class Band(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Event name must be greater than 1 character")]
    )
    event = models.ForeignKey('Event', models.CASCADE, null=False, related_name='bands')
    members = models.ManyToManyField('Member', through='BandMember', related_name='bands')

    # Shows up in the admin list
    def __str__(self):
        """String for representing the Bands object."""
        return self.name
    
class BandMember(models.Model):
    band = models.ForeignKey('Band', models.CASCADE, null=False)
    member = models.ForeignKey('Member', models.CASCADE, null=False)

    def __str__(self):
        """String for representing the BandMembers object."""
        return f"{self.member} IN {self.band}"
    
class Practice(models.Model):
    band = models.ForeignKey('Band', models.CASCADE, null=False)

    date = models.DateField()

    startTime = models.TimeField()

    endTime = models.TimeField()
    
    class Meta:
        ordering = ['date','startTime']

    def __str__(self):
        """String for representing the Practices object."""
        return f"[{self.date}] {self.band} from {self.startTime} to {self.endTime}"
    
