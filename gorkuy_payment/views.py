from django.shortcuts import render
from database.models import Reservasi,Pembayaran
# Create your views here.
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def bayar(request):
    try:
        reservasi = Reservasi.objects.get(pk=request.data['reservasi_id'])
        lapangan = reservasi.lapangan
        jumlah_jadwal = lapangan.jadwal_set.count()
        harga = lapangan.harga_perJam * jumlah_jadwal
        rekening = reservasi.penyewa.get_rekening()
        if rekening.saldo > harga:
            rekening.decrease_balance(harga)
            payment = Pembayaran.create(reservasi=reservasi)
            payment.save()
            data = PembayaranSerializer(payment).data
            return Response(data)
        else:
            return Response({"status":"failed","error_message":"saldo tidak cukup"},status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"status":"failed","error_message":"terjadi error pada pembayaran","error":f"{e}"},status=status.HTTP_400_BAD_REQUEST)




