from django.shortcuts import render, get_object_or_404, redirect
from database.models import *
from .forms import *
# Create your views here.
def show_reservasi(request):
    user = request.user
    list_reservasi = Reservasi.objects.filter(penyewa=user)
    context = {'list_reservasi':list_reservasi}
    return render(request, 'daftar-reservasi.html', context)

def reschedule_reservasi(request, id):
    reservasi = get_object_or_404(Reservasi, id)
    form = RescheduleForm()
    if request.method == 'POST':
        reservasi.jadwal = request.POST['jadwal']
        reservasi.save()
        return redirect('reschedule:show_reservasi')

    context = {'form':form}
    return render(request, 'reschedule:reschedule_reservasi', context)