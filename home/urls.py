from django.urls import path
from .views import HomeView, DetailStudentView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('detail/<slug:my_slug>/', DetailStudentView.as_view(), name='detail'),
]
