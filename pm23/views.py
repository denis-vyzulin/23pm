from django.shortcuts import render
from .models import Lesson
from datetime import datetime, timedelta
from django.conf import settings


def shedule(request):
    monday = settings.REF_POINT
    today = datetime.now() + timedelta(days=4)
    diff = (today - monday).days
    monday += timedelta(days=(diff - diff % 7))
    dates = []
    for week in range(2):
        first_day = monday + timedelta(days=week*7)
        tmp = []
        for i in range(6):
            tmp.append(first_day + timedelta(days=i))
        dates.append(tmp)

    current_week = diff // 7 + 1
    print(dates, current_week)
    if current_week % 2 == 0:
        dates = [dates[1], dates[0]]

    context = {
        '23pm_odd': Lesson.objects.filter(week_type='Odd').order_by('time_start'),
        '23pm_even': Lesson.objects.filter(week_type='Even').order_by('time_start'),
        'dates': dates,
        'today': today,
        'curr_week': current_week,
        'curr_week_type': current_week % 2,
    }
    return render(request, 'pm23/shedule.html', context=context)
