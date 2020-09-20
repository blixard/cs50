from django.shortcuts import render
from datetime import datetime

def index(request):
    now = datetime.now();
    return render(request, "date/index.html",{
        "month":now.month,
        "day": now.day,
        "year": now.year,
        "hour":now.hour,
        "minute":now.minute,
        "sec":now.second
    })
