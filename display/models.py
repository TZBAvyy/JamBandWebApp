from django.db import models
from django.core.validators import MinLengthValidator


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

    def __str__(self):
        """String for representing the Members object."""
        return self.name
    
class MemberSection(models.Model):
    class Proficiency(models.IntegerChoices):
        BEGINNER = 1
        NOVICE = 2
        ADEPT = 3
        SKILLED = 4
        EXPERT = 5
    
    proficiency = models.IntegerField(choices=Proficiency)

    section = models.ForeignKey('Section', on_delete=models.CASCADE, null=False)

    member = models.ForeignKey('Member', on_delete=models.CASCADE, null=False)

    def __str__(self):
        """String for representing the MemberSections object."""
        return f"{self.member} (Level {self.proficiency} {self.section})"


class Event(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Event name must be greater than 1 character")]
    )
    date = models.DateField()
    
    time = models.TimeField()

    # Shows up in the admin list
    def __str__(self):
        """String for representing the Events object."""
        return self.name
    
class Band(models.Model):
    name = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Event name must be greater than 1 character")]
    )
    event = models.ForeignKey('Event', models.CASCADE, null=False)

    # Shows up in the admin list
    def __str__(self):
        """String for representing the Bands object."""
        return self.name
    
class BandMember(models.Model):
    band = models.ForeignKey('Band', models.CASCADE, null=False)

    section = models.ForeignKey('Section', models.CASCADE, null=False)

    member = models.ForeignKey('Member', models.CASCADE, null=False)

    def __str__(self):
        """String for representing the BandMembers object."""
        return f"{self.member} ({self.section}) IN {self.band}"
    
class Practice(models.Model):
    band = models.ForeignKey('Band', models.CASCADE, null=False)

    date = models.DateField()

    startTime = models.TimeField()

    endTime = models.TimeField()

    def __str__(self):
        """String for representing the Practices object."""
        return f"{self.band} ON {self.date} FROM {self.startTime} TO {self.endTime}"
    
