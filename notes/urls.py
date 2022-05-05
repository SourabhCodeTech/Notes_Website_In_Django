from notes import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('notes/', views.notes, name='notes'),
]
