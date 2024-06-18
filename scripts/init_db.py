import csv
from display.models import Member,Section,MemberSection
from django.contrib.auth.models import User
from settings.models import UserProfile
from decouple import config

def run():
    with open("hidden/AY23_24 Members Details.csv",'r') as file:
        reader = csv.DictReader(file)
        print("File Opened")

        #Reset DB
        Member.objects.all().delete()
        Section.objects.all().delete()
        MemberSection.objects.all().delete()
        User.objects.all().delete()

        #Create default user and superuser (REMEMBER TO UPDATE .env FILE)
        user = User.objects.create_user(username="jambandmember",password=config("DEFAULTUSERPASS"))
        user.first_name = "Member Account"
        user.save()
        UserProfile.objects.get_or_create(user=user)

        user = User.objects.create_superuser(username="hallonejamband",password=config("SUPERUSERPASS"),email='hallonejamband@gmail.com')
        user.first_name = "CoChair Account"
        user.save()
        UserProfile.objects.get_or_create(user=user)

        print("Delete complete, starting insertion")
        for row in reader:
            member = Member.objects.get_or_create(name = row["Name"])[0]
            section = Section.objects.get_or_create(instrument=row["Main Role"])[0]
            MemberSection.objects.get_or_create(proficiency=2,section=section,member=member)

            #Create User model instance for each member
            user = User.objects.create_user(username=row["Matric Number"].upper(),password=config("DEFAULTUSERPASS"))
            user.first_name = row["Name"]
            user.save()
            UserProfile.objects.get_or_create(user=user,member=member)
            
            #Create Member - Section Junction for each Sub Role
            for i in range(1,4):
                if row[f"Sub Role {i}"] == "": #Checks for blank sub role
                    break
                elif row[f"Sub Role {i}"][-3:] == "(L)": #Checks if learner or not
                    role = row[f"Sub Role {i}"][:-3]
                    proficiency = 1
                else:
                    role = row[f"Sub Role {i}"]
                    proficiency = 2
                section = Section.objects.get_or_create(instrument=role)[0]
                MemberSection.objects.get_or_create(proficiency=proficiency,section=section,member=member)
    print("DB has been initialised")

