from django.urls import path
from .views import HomeView, DetailStudentView, CreateStudentView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateStudentView.as_view(), name='create'),
    path('detail/<slug:my_slug>/', DetailStudentView.as_view(), name='detail'),
]
