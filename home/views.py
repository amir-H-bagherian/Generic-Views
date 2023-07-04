from typing import Any, Dict, Optional
from django.shortcuts import render
from django.views import View
from django.views.generic import RedirectView, TemplateView, ListView
from .models import Student


class HomeView(ListView):
    template_name = 'home/home.html'
    model = Student
    context_object_name = 'student'
    ordering = '-age'