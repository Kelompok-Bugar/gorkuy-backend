from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(UserGorkuy,UserAdmin)
admin.site.register(Mitra)
admin.site.register(Penyewa)
admin.site.register(Jadwal)
admin.site.register(Lapangan)
admin.site.register(Reservasi)
admin.site.register(Pembayaran)
admin.site.register(Rekening)
admin.site.register(RekeningPayKuy)
