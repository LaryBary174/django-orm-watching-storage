from datacenter.models import Passcard
from datacenter.models import Visit
from datacenter.formatting_units_for_temp import format_duration
from django.shortcuts import render


def storage_information_view(request):
    non_leave_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for non_leave_visit in non_leave_visits:
        name_non_leave_visit = non_leave_visit.passcard.owner_name
        entered_at = non_leave_visit.entered_at
        duration_not_format = non_leave_visit.get_duration()
        duration = format_duration(duration_not_format.total_seconds())
        non_closed_visits.append(
            {
                'who_entered': name_non_leave_visit,
                'entered_at': entered_at,
                'duration': duration,
            }
        )

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)

