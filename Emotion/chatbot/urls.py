from django.urls import path
from chatbot import views

urlpatterns = [
    path('', views.home),
    path('query', views.query),
]
