from datetime import datetime
from django.utils.timezone import localtime

from django.db import models


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def get_duration(self):
        if localtime(self.leaved_at):
            duration = localtime(self.leaved_at) - localtime(self.entered_at)
        else:
            duration = datetime.now() - localtime(self.entered_at)
        return duration


    def is_visit_long(self, minutes=60):
        duration_seconds = self.get_duration().total_seconds()
        if duration_seconds / 60 > minutes :
            return True
        return False

def format_duration(seconds):
    hours = int(seconds) // 3600
    minutes = (int(seconds) % 3600) // 60
    return f'{hours}ч {minutes}мин'