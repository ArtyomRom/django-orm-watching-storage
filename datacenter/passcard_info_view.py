from datacenter.models import Passcard, Visit
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from datacenter.duration_helper import is_visit_long, get_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all().filter(passcode=passcode)
    get_object_or_404(passcard)
    visits = Visit.objects.filter(passcard=passcard[0])
    this_passcard_visits = [
        {
            'entered_at': visit.entered_at,
            'duration': get_duration(visit.entered_at, visit.leaved_at),
            'is_strange': is_visit_long(visit),
        } for visit in visits
    ]
    context = {
        'passcard': passcard[0],
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
