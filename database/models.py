from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime as dt

# Create your models here.
class UserGorkuy(AbstractUser):
    username = models.CharField(max_length=255,primary_key=True)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

class Mitra(UserGorkuy):
    bankAccount = models.CharField(max_length=255)
    ## List Lapangan

class Penyewa(UserGorkuy):
    ## List daftarReservasi
    pass

class Lapangan(models.Model):
    id = models.AutoField(primary_key=True)
    mitra = models.ForeignKey(Mitra,on_delete=models.CASCADE)
    jenis_choices = (
        ("Futsal", "Futsal"),
        ("Bulutangkis","Bulutangkis"),
        ("Basket","Basket")
    )
    jenis = models.CharField(choices=jenis_choices,max_length=50,default="Futsal")
    harga_perjam = models.IntegerField()
    jam_buka = models.TimeField(default=dt.time(00, 00))
    jam_tutup = models.TimeField(default=dt.time(23, 00))
    

class Jadwal(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    tanggal = models.DateField()
    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)

class Reservasi(models.Model):
    id = models.AutoField(primary_key=True)
    tanggal = models.DateField(auto_now_add=True)
    penyewa = models.ForeignKey(Penyewa,on_delete=models.CASCADE)
    lapangan = models.ForeignKey(Lapangan,on_delete=models.CASCADE)
    jadwal = models.ForeignKey(Jadwal,on_delete=models.CASCADE,blank=True,null=True)
    totalHarga = models.IntegerField()
    ## Pembayaran

class Pembayaran(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    jumlah = models.IntegerField()
    reservasi = models.ForeignKey(Reservasi, on_delete=models.CASCADE)


