from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [
    path('home', TemplateView.as_view(template_name='home.html')),
]