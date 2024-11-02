from django.utils.timezone import localtime
from pytz import timezone as pytz_timezone
import time


def get_duration(start, end):
    total_time = (localtime(end) - localtime(start)).total_seconds()
    return time.strftime('%H:%M', time.gmtime(total_time))


def format_duration(time):
    moscow_tz = pytz_timezone('Europe/Moscow')
    return localtime(time, timezone=moscow_tz)


def is_visit_long(visit, minutes=60):
    if visit.leaved_at is None:
        return 'В хранилище'
    start_time = localtime(visit.entered_at)
    finish_time = localtime(visit.leaved_at)
    total_time = ((finish_time - start_time).total_seconds()) // 60
    return minutes < total_time