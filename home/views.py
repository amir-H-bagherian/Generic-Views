from typing import Any, Dict, Optional
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from django.views.generic import RedirectView, TemplateView, ListView
from django.views.generic import DetailView, FormView
from .models import Student
from .forms import ContactForm
from django.urls import reverse_lazy

class HomeView(ListView):
    template_name = 'home/home.html'
    context_object_name = 'student'
    ordering = '-age'
    allow_empty = False
    paginate_by = 2
    
    def get_queryset(self) -> QuerySet[Any]:
        return Student.objects.all()
    
class DetailStudentView(DetailView):
    template_name = 'home/detail.html'
    context_object_name = 'student'
    slug_field = 'first_name'
    slug_url_kwarg = 'my_slug'

    def get_queryset(self) -> QuerySet[Any]:
        return Student.objects.filter(age__gt=30)
    
class ContactView(FormView):
    template_name = 'home/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')