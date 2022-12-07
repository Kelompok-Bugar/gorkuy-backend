from django.urls import path
from .views import *

app_name = "reservasi"

urlpatterns = [
    path("<int:id>", add_reservasi, name="add_reservasi"),
]
