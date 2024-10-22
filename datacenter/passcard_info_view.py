from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.models import format_duration
from django.shortcuts import render
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    pass_owner_name = passcard.owner_name
    passcard_visits = passcard.visit_set.all()
    this_passcard_visits = []
    for visit in passcard_visits:
        entered_at = visit.entered_at
        duration = format_duration(visit.get_duration().total_seconds())
        is_strange = visit.is_visit_long()
        this_passcard_visits.append(
            {
                'entered_at': entered_at,
                'duration': duration,
                'is_strange': is_strange
            }
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
