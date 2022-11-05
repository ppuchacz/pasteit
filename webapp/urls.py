from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/<int:id>/', views.note, name='note'),
]