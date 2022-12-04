from django.urls import path
from .views import *

urlpatterns = [
    path('pay/',bayar,name="pay"),
]