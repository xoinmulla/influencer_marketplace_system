from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_analytics, name='analytics_list'),
]
