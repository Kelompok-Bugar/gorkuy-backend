from django.shortcuts import render
from database.models import Reservasi,Pembayaran
# Create your views here.
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

def payment_page(request,reservasi_id):
    reservasi = Reservasi.objects.get(id=reservasi_id)
    if request.method == 'GET':
        print(f"reservasinya {reservasi_id}")
        data = {'reservasi' : reservasi}
    elif request.method == 'POST':
        try: 
            if reservasi.is_paid:
                return render(request,'error.html')
            lapangan = reservasi.lapangan
            harga = reservasi.totalHarga
            if request.POST['jenisRekening'] == 'GorPay':
                rekening = reservasi.penyewa.get_rekening()
            else:
                rekening = reservasi.penyewa.get_rekening2()
            if rekening.saldo > harga:
                rekening.decrease_balance(harga)
                rekening.save()
                payment = Pembayaran.objects.create(reservasi=reservasi)
                payment.save()
                reservasi.is_paid = True
                reservasi.save()
                data = PembayaranSerializer(payment).data
                return render(request,'success.html')
            else:
                return render(request,'failed.html')
        except Exception as e:
            return render(request,'error.html')
    return render(request,'payment.html',data)


