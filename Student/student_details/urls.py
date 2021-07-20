from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.register, name='student-register'),
    path('about/', views.about, name='student-about')
]
