from typing import Any, Dict, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from django.views.generic import RedirectView, TemplateView, ListView
from .models import Student


class HomeView(ListView):
    template_name = 'home/home.html'
    context_object_name = 'student'
    ordering = '-age'
    allow_empty = False
    paginate_by = 1
    
    def get_queryset(self) -> QuerySet[Any]:
        return Student.objects.all()
    
    