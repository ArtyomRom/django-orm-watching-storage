from datacenter.models import Visit
from django.shortcuts import render
from datacenter.duration_helper import format_duration, get_duration, is_visit_long


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
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
