from typing import Any, Dict, Optional
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import RedirectView, TemplateView, ListView, DeleteView
from django.views.generic import DetailView, FormView, CreateView, UpdateView
from .models import Student, Comment
from .forms import ContactForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

class HomeView(ListView):
    template_name = 'home/home.html'
    context_object_name = 'student'
    ordering = '-age'
    allow_empty = False
    paginate_by = 10
    
    def get_queryset(self) -> QuerySet[Any]:
        return Student.objects.all()
    
class DetailStudentView(DetailView):
    template_name = 'home/detail.html'
    context_object_name = 'student'
    slug_field = 'first_name'
    slug_url_kwarg = 'my_slug'

    def get_queryset(self) -> QuerySet[Any]:
        return Student.objects.all()
    
class CreateStudentView(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'home/create.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.cleaned_data['age'] < 10:
            raise ValueError("Not a valid age")
        return super().form_valid(form)
    
class UpdateStudentView(UpdateView):
    model = Student
    fields = ['age']
    template_name = 'home/create.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        if form.cleaned_data['age'] < 10:
            raise ValueError("Not a valid age")
        return super().form_valid(form)
    
class DeleteStudentView(DeleteView):
    model = Student
    success_url = reverse_lazy('home')
    template_name = 'home/delete.html'
    
class StudentLoginView(LoginView):
    template_name = 'home/login.html'
    next_page = reverse_lazy('home')