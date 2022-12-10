from typing import OrderedDict
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from database.models import Reservasi,Lapangan,Jadwal,Penyewa,UserGorkuy,Mitra
import json
from django.http.response import HttpResponse
# Create your views here.

def reservasi(request):
    if request.method == 'POST':
        
        if request.user.is_anonymous | isinstance(request.user,UserGorkuy) | isinstance(request.user,Mitra):
            user = Penyewa.objects.get(username = 'admin2')
        
       
        data = request.body.decode('utf-8')
        body = json.loads(data) 
        print(body)
        # TODO(Rey) : save the reservation and redirect to payment page
        tanggal = body['date']
        id_reservasi = body['reservasi_id']
        id_lapangan = body['lapangan']
        reservasi = Reservasi.objects.get(id = id_reservasi )
        lapangan = Lapangan.objects.get(id=id_lapangan)
        reservasi.penyewa = user
        reservasi.lapangan = lapangan
        reservasi.save()
        for i in body['hours']:
            start = i[0:4]
            end = i[6:10]
            jadwal = Jadwal.objects.create(start = start, end = end, reservasi=reservasi, lapangan=lapangan, tanggal = tanggal)
            jadwal.save
        
        data = {"success" : True}
        response = json.JSONEncoder().encode(data)
        return HttpResponse(response, content_type="application/json")
    
    reservasi_obj = Reservasi.objects.create()
    reservasi_obj.save
    print(reservasi_obj.id)
    response_data = {'id':reservasi_obj.id}
    return HttpResponse(json.dumps(response_data), content_type="application/json") 

def add_reservasi(request,id):
    
    # user = request.user
    
    # form_1 = DateForm()
    
    # if request.method == 'POST':
    #     print("halo")
    #     form_1 = DateForm(request.POST)
    #     if form_1.is_valid():
    #         date = request.POST.get('reserve_date')
    #         print((date))
    #         list_jadwal = list_jadwal_tersedia(lapangan,date)
    #         context = {'form_1': form_1,'id':id}
    #         return render(request,template_name="h.html",context=context)
        # form.fields['jadwal'].choices = list_jadwal
        # if form.is_valid():
        #     form.save()
        #     return redirect('/') # redirect ke halaman pembayaran
    lapangan = get_object_or_404(Lapangan,id=id)
    jam_buka = lapangan.jam_buka
    jam_tutup = lapangan.jam_tutup
    biaya = lapangan.harga_perjam
    nama = lapangan.mitra.name
    context = {'id':id,
               'nama':nama,
               'jam_buka':jam_buka,
               'jam_tutup':jam_tutup,
               'biaya':biaya}
    

    return render(request,template_name="h.html",context = context)


def list_jadwal_tersedia(request, id, date):
    lapangan = get_object_or_404(Lapangan,id=id)
    jam_buka = int(lapangan.jam_buka.strftime("%H"))
    jam_tutup = int(lapangan.jam_tutup.strftime("%H"))
    
    jadwal = Jadwal.objects.filter(lapangan=lapangan,tanggal=date)
    booked_jadwal = list(jadwal)
    list_jadwal = []
    booked_jadwal = [getattr(j,'start').strftime("%H") for j in booked_jadwal]
    for i in range(jam_buka,jam_tutup):
        if str(i) in booked_jadwal:
            continue
        j = i+1
        formatted_j = str(j)+":00"
        formatted_i = str(i)+":00"
        if j<10:
            formatted_j = "0"+formatted_j
        if i<10:
            formatted_i = "0"+formatted_i
        formatted_time = formatted_i + "-" + formatted_j
        list_jadwal.append(formatted_time)
    print()
    print()
    print("jam buka lapangan:",jam_buka)
    print("jam buka lapangan:",jam_tutup)
    print("jadwal yg tersedia:",list_jadwal)

    data = {"hours" : list_jadwal}
    response = json.JSONEncoder().encode(data)
    return HttpResponse(response, content_type="application/json")



    
    