from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(UserGorkuy,UserAdmin)
admin.site.register(Mitra)
admin.site.register(Penyewa)
<<<<<<< HEAD
admin.site.register(Jadwal)
admin.site.register(Lapangan)
admin.site.register(Reservasi)
admin.site.register(Pembayaran)
admin.site.register(Rekening)
admin.site.register(RekeningPayKuy)
=======
admin.site.register(Lapangan)
admin.site.register(Jadwal)
admin.site.register(Reservasi)
admin.site.register(Pembayaran)
>>>>>>> 16f5f24864123ee510506f0513ea1f8f525fae2b
