from django.urls import path
from . import views

urlpatterns = [
    path('', views.modsmanager_home, name='modsmanager_home'),
    path('modtranslations/', views.modtranslations, name='modtranslations'),
]
