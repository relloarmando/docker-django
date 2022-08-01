from django import forms
from django_celery_beat.models import PeriodicTask, IntervalSchedule


class PeriodicTaskForm(forms.ModelForm):
    class Meta:
        model = PeriodicTask
        fields = ['name', 'task', 'description', 'interval', 'args', 'enabled', 'start_time']


class IntervalForm(forms.ModelForm):
    class Meta:
        model = IntervalSchedule
        fields = '__all__'
