from django.urls import path
from . import views


app_name = 'pm23'
urlpatterns = [
    path('', views.shedule, name='shedule'),
]