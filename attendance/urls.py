from django.urls import path
from . import views

urlpatterns = [
    path('', views.students, name='students'),
    path('attendance/', views.mark_attendance, name='attendance'),
    path('records/', views.records, name='records'),
]