from django.urls import path
from .views import *

urlpatterns = [
    path('<int:id>', show_edit_form, name='show_edit_form'),
    path('save/<int:id>', edit_jadwal, name='edit_jadwal'),   
]
