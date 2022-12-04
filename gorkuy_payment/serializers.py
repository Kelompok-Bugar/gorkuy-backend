from rest_framework import serializers
from database.models import Pembayaran

class PembayaranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pembayaran
        fields = '__all__'