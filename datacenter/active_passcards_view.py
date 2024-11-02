from datacenter.models import Passcard, Visit
from django.shortcuts import render


def active_passcards_view(request):
    all_passcards = Passcard.objects.all()
    all_visits = Visit.objects.all()
    context = {
        'active_passcards': all_passcards.filter(is_active=True),
        'visit': all_visits.filter(leaved_at=None),

    }
    return render(request, 'active_passcards.html', context)
