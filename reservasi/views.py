from typing import OrderedDict
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservasiForm
from django.contrib.auth.decorators import login_required
import random
from django.http import HttpResponse,  JsonResponse
from django.template.loader import render_to_string 
from database.models import Reservasi,Lapangan,Jadwal
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def add_reservasi(request,id):
    
    user = request.user
    lapangan = get_object_or_404(Lapangan,id=id)
    jam_buka = int(lapangan.jam_buka.strftime("%H"))
    jam_tutup = int(lapangan.jam_tutup.strftime("%H"))
    jadwal = Jadwal.objects.filter(lapangan=lapangan).all().values()
    booked_jadwal = list(jadwal)
    list_jadwal = []
    # list jadwal yang tersedia
    # booked_jadwal = [i.value for i in booked_jadwal]
    # for i in range(jam_buka,jam_tutup):
    #   if booked_jadwal.contains(i):
    #      pass
    #   else:
    #       list_jadwal.append(i)
    
    form = ReservasiForm()
    form.fields['jadwal'].choices = list_jadwal
    
    if request.method == 'POST':
        form = ReservasiForm(request.POST)
        form.fields['jadwal'].choices = list_jadwal
        if form.is_valid():
            form.save()
            return redirect('/') # redirect ke halaman pembayaran
    
    context = {'form': form,
               'id':id}
    print(id)
    print(lapangan)
    print(jadwal)
    print(jam_buka)

    return render(request,template_name="lapanganDetail.html",context = context)
    