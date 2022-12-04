from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ObjectDoesNotExist
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
    

class Jadwal(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    tanggal = models.DateField()
    lapangan = models.ForeignKey(Lapangan, on_delete=models.CASCADE)

class Reservasi(models.Model):
    id = models.AutoField(primary_key=True)
    tanggal = models.DateField(auto_now_add=True)
    penyewa = models.ForeignKey(Penyewa,on_delete=models.CASCADE)
    lapangan = models.OneToOneField(Lapangan,on_delete=models.CASCADE)
    jadwal_dipilih  = models.ForeignKey(Jadwal,on_delete=models.CASCADE)
    ## Pembayaran

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

