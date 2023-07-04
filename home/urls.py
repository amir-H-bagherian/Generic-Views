from django.urls import path
from .views import HomeView, FisrtView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('first/', FisrtView.as_view(), name='first'),
]
