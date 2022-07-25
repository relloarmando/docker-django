from django.urls import path

from first_app import views

urlpatterns = [
    path('my-first-page', views.home_view, name="first_page"),
]
