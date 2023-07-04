from django.shortcuts import render
from django.views import View
from django.views.generic import RedirectView, TemplateView
from .models import Student


class HomeView(TemplateView):
    template_name = 'home/home.html'

class FisrtView(RedirectView):
    url = '/'