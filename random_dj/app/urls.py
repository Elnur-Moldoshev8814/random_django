from django.urls import path

from .import views

urlpatterns = [
    path('random/<int:num>/', views._random),
    path('palindrom/<str:text>/', views.palindrom)
]