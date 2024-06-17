import csv
from display.models import Member,Section,MemberSection

def run():
    with open("hidden/AY23_24 Members Details.csv",'r') as file:
        reader = csv.DictReader(file)
        print("File Opened")

        #Reset DB
        Member.objects.all().delete()
        Section.objects.all().delete()
        MemberSection.objects.all().delete()

        print("Delete complete, starting insertion")
        for row in reader:
            member = Member.objects.get_or_create(name = row["Name"])[0]
            section = Section.objects.get_or_create(instrument=row["Main Role"])[0]
            MemberSection.objects.get_or_create(proficiency=2,section=section,member=member)

            for i in range(1,4):
                if row[f"Sub Role {i}"] == "":
                    break
                elif row[f"Sub Role {i}"][-3:] == "(L)":
                    role = row[f"Sub Role {i}"][:-3]
                    proficiency = 1
                else:
                    role = row[f"Sub Role {i}"]
                    proficiency = 2
                section = Section.objects.get_or_create(instrument=role)[0]
                MemberSection.objects.get_or_create(proficiency=proficiency,section=section,member=member)
    print("DB has been initialised")

