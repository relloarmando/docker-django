from django.urls import reverse
from django.views.generic import ListView, CreateView
from django_celery_beat.models import PeriodicTask

from celery_example.forms import PeriodicTaskForm, IntervalForm


class HomeView(ListView):
    model = PeriodicTask
    template_name = 'home.html'


class PeriodicTaskView(CreateView):
    template_name = 'task_form.html'
    form_class = PeriodicTaskForm

    def get_success_url(self):
        return reverse('first_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_interval"] = IntervalForm
        return context


class IntervalView(CreateView):
    template_name = 'task_form.html'
    form_class = IntervalForm

    def get_success_url(self):
        return reverse('new_periodic_task')
