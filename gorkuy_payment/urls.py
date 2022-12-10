from django.urls import path
from .views import *

urlpatterns = [
    path('pay/<int:reservasi_id>',payment_page,name='payment_page')
    
]