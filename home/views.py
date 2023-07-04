from typing import Any, Dict, Optional
from django.shortcuts import render
from django.views import View
from django.views.generic import RedirectView, TemplateView
from .models import Student


class HomeView(TemplateView):
    template_name = 'home/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print('another time')
        print(kwargs)
        context["name"] = kwargs['name']
        context["age"] = kwargs['age']
        return context
    

class FisrtView(RedirectView):
    pattern_name = 'home'
    
    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        print(kwargs)
        return super().get_redirect_url(*args, **kwargs)