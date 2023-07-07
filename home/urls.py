from django.urls import path
from .views import HomeView, DetailStudentView, CreateStudentView, UpdateStudentView, DeleteStudentView, StudentLoginView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateStudentView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('login/', StudentLoginView.as_view(), name='login'),
    path('delete/<int:pk>/', DeleteStudentView.as_view(), name='delete'),
    path('detail/<slug:my_slug>/', DetailStudentView.as_view(), name='detail'),
]
