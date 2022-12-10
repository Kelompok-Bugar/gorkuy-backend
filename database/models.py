from django.db import models
from django.contrib.auth.models import AbstractUser
<<<<<<< HEAD
from django.core.exceptions import ObjectDoesNotExist
=======
import datetime as dt

>>>>>>> 16f5f24864123ee510506f0513ea1f8f525fae2b
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
    def get_rekening(self):
        try:
            return self.rekening
        except ObjectDoesNotExist:
            return None
    def get_rekening2(self):
        try:
            return self.rekeningpaykuy
        except ObjectDoesNotExist:
            return None

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
    

class Reservasi(models.Model):
    id = models.AutoField(primary_key=True)
    tanggal = models.DateField(auto_now_add=True)
    penyewa = models.ForeignKey(Penyewa,on_delete=models.CASCADE,blank=True,null=True)
    lapangan = models.ForeignKey(Lapangan,on_delete=models.CASCADE,blank=True,null=True)
    
    totalHarga = models.IntegerField(blank=True,null=True)
<<<<<<< HEAD
    is_paid = models.BooleanField(default=False)
=======
>>>>>>> 16f5f24864123ee510506f0513ea1f8f525fae2b
    ## Pembayaran

class Jadwal(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    tanggal = models.DateField()
    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)
    reservasi = models.ForeignKey(Reservasi,on_delete=models.CASCADE,blank=True,null=True)

class Pembayaran(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(auto_now_add=True)
    reservasi = models.ForeignKey(Reservasi, on_delete=models.CASCADE)

class Rekening(models.Model):
    penyewa = models.OneToOneField(Penyewa,on_delete=models.CASCADE,primary_key= True)
    saldo = models.BigIntegerField(default=0)

    def decrease_balance(self,amount):
        self.saldo -= amount
        if self.saldo < 0:
            self.saldo = 0
        return self.saldo

class RekeningPayKuy(models.Model):
    penyewa = models.OneToOneField(Penyewa,on_delete=models.CASCADE,primary_key= True)
    saldo = models.BigIntegerField(default=0)

    def decrease_balance(self,amount):
        self.saldo -= amount
        if self.saldo < 0:
            self.saldo = 0
        return self.saldo

