from django.urls import path
from .views import HomeView, FisrtView

urlpatterns = [
    path('a/<str:name>/<int:age>/', HomeView.as_view(), name='home'),
    path('first/<str:name>/<int:age>/', FisrtView.as_view(), name='first'),
]
