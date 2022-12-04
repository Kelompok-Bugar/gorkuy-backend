from django.urls import path
from .views import *

app_name = "reservasi"

urlpatterns = [
    path("<str:id>/reservasi", add_reservasi, name="add_reservasi"),
]
