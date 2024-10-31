from datacenter.models import Visit, is_visit_long
from django.shortcuts import render
from django.utils.timezone import localtime
from pytz import timezone as pytz_timezone
import time


def get_duration(start, end):
    total_time = (localtime(end) - localtime(start)).total_seconds()
    return time.strftime('%H:%M', time.gmtime(total_time))


def format_duration(time):
    moscow_tz = pytz_timezone('Europe/Moscow')
    return localtime(time, timezone=moscow_tz)




def storage_information_view(request):
    visitors = Visit.objects.all()
    non_closed_visits = [
        {
            'who_entered': visitor.passcard.owner_name,
            'entered_at': format_duration(visitor.entered_at),
            'duration': get_duration(visitor.entered_at, visitor.leaved_at),
            'suspicious': is_visit_long(visitor)
        } for visitor in visitors.filter(leaved_at=None)
    ]

    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
