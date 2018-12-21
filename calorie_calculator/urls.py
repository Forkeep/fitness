from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    path('cal_calulator/',views.cal_calculator),
    path('cal_power/',views.power_calculator),

]