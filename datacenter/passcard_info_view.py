from datacenter.models import Passcard, Visit, is_visit_long
from django.shortcuts import render
from datacenter.storage_information_view import get_duration
from django.shortcuts import get_object_or_404

def my_view(request):
    obj = get_object_or_404(request, pk=1)

def passcard_info_view(request, passcode):
    passcard = Passcard.objects.all().filter(passcode=passcode)[0]
    visits = Visit.objects.all().filter(passcard=passcard.id)

    this_passcard_visits = [
        {
            'entered_at': visit.entered_at,
            'duration': get_duration(visit.entered_at, visit.leaved_at),
            'is_strange': is_visit_long(visit),
        } for visit in visits
    ]
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
