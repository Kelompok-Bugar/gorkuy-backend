from django.urls import path
from .views import index, search


urlpatterns = [
    path('<str:keyword>/', search),
    path('', index)
]

