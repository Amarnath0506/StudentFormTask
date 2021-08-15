from django.contrib.auth import views
from django.urls import path
from .views import StudentUploadView

urlpatterns = [
    path('importcsv/', StudentUploadView.as_view(), name='importstudent')
]