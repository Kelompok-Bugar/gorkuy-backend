from django.urls import path
from .views import *

app_name = 'reschedule'

urlpatterns = [
    path('', show_reservasi, name='show_reservasi'),
    path('<int:id>/', reschedule_reservasi, name='reschedule_reservasi'),
]