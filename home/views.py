from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import Student


class HomeView(TemplateView):
    template_name = 'home/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["student"] = Student.objects.all()
        return context
    