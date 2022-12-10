from typing import OrderedDict
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservasiForm,DateForm
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
    
    
    
    form_1 = DateForm()
    
    if request.method == 'POST':
        print("halo")
        form_1 = DateForm(request.POST)
        if form_1.is_valid():
            date = request.POST.get('reserve_date')
            
            list_jadwal = list_jadwal_tersedia(lapangan,date)
            context = {'form_1': form_1,'id':id}
            return render(request,template_name="h.html",context=context)
        # form.fields['jadwal'].choices = list_jadwal
        # if form.is_valid():
        #     form.save()
        #     return redirect('/') # redirect ke halaman pembayaran
    
    context = {'form_1': form_1,
               'id':id}
    

    return render(request,template_name="h.html",context = context)

def late(self):
    return self.time.hour > 9


def list_jadwal_tersedia(lapangan,date):
    
    jam_buka = int(lapangan.jam_buka.strftime("%H"))
    jam_tutup = int(lapangan.jam_tutup.strftime("%H"))
    
    jadwal = Jadwal.objects.filter(lapangan=lapangan,tanggal=date)
    booked_jadwal = list(jadwal)
    list_jadwal = []
    booked_jadwal = [getattr(j,'start').strftime("%H") for j in booked_jadwal]
    for i in range(jam_buka,jam_tutup):
      if str(i) in booked_jadwal:
         pass
      else:
          list_jadwal.append(i)
    print()
    print()
    print("jam buka lapangan:",jam_buka)
    print("jam buka lapangan:",jam_tutup)
    print("jadwal yg tersedia:",list_jadwal)
    
    return list_jadwal



    
    