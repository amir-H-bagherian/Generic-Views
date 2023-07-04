from django.urls import path
from .views import HomeView, DetailStudentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('detail/<slug:my_slug>/', DetailStudentView.as_view(), name='detail'),
]
