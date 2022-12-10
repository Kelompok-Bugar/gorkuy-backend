from django.urls import path
from .views import *

app_name = "reservasi"

urlpatterns = [
    path("<int:id>", add_reservasi, name="add_reservasi"),
    path("api/<int:id>/<str:date>", list_jadwal_tersedia),
    path("api/reserve", reservasi)
]
