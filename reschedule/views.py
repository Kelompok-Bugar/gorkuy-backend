from django.shortcuts import render
from database.models import *
# Create your views here.
def show_reservasi(request):
    user = request.user
    list_reservasi = Reservasi.objects.filter(penyewa=user)
    context = {'list_reservasi':list_reservasi}
    return render(request, 'daftar-reservasi.html', context)

def reschedule_reservasi(request, id):
    pass