from django.urls import path
from . import views

urlpatterns = [
    path('input/', views.input_view, name='input_view'),
    path('display/', views.display_view, name='display_view'),
    path('session/', views.session_view, name='session_view'),
]
