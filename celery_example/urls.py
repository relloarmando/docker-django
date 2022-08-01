from django.urls import path

from celery_example import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="first_page"),
    path('periodic_task_new/', views.PeriodicTaskView.as_view(), name="new_periodic_task"),
    path('interval_new/', views.IntervalView.as_view(), name="new_interval"),
]
