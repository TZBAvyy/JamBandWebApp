from display.models import Practice
from datetime import datetime as dt
from time import sleep

def run():
    print("Running deletion script of expired Practice objects")
    current_date = dt.now().date()
    dates_to_delete = Practice.objects.filter(date__lt=current_date)
    sleep(1)
    if dates_to_delete:
        dates_to_delete.delete()
        print("Deleted!")
    else:
        print("Nothing to delete! Time to sleep!")