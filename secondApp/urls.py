from django.urls import path
from . import views

urlpatterns = [
    path('greetings/', views.functionName)
]