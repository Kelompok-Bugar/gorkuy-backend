from django.shortcuts import render, get_object_or_404
from database.models import *
# Create your views here.
def reschedule(request,id):
    
    user = request.user
    lapangan = get_object_or_404(Lapangan,id=id)
    jam_buka = int(lapangan.jam_buka.strftime("%H"))
    jam_tutup = int(lapangan.jam_tutup.strftime("%H"))
    jadwal = Jadwal.objects.filter(Lapangan=lapangan).all().values()
    booked_jadwal = list(jadwal)
    list_jadwal = []
    # list jadwal yang tersedia
    booked_jadwal = [i.value for i in booked_jadwal]
    for i in range(jam_buka,jam_tutup):
      if booked_jadwal.contains(i):
         pass
      else:
          list_jadwal.append(i)
    
    form = ReservasiForm()
    form.fields['jadwal'].choices = list_jadwal
    
    if request.method == 'POST':
        form = ReservasiForm(request.POST)
        form.fields['jadwal'].choices = list_jadwal
        if form.is_valid():
            form.save()
            return redirect('/') # redirect ke halaman pembayaran
    
    context = {'form': form}
    return render(request,'',context)