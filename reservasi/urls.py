from django.urls import path
from .views import *

app_name = "reservasi"

urlpatterns = [
    path("lapangan/<int:id>", add_reservasi, name="add_reservasi"),
    path("lapangan/api/<int:id>/<str:date>", list_jadwal_tersedia),
    path("lapangan/api/reserve", reservasi),
    #path("lapangan/payment/<int:id>", pembayaran),
]
