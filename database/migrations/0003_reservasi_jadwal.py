# Generated by Django 4.1.3 on 2022-12-06 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_lapangan_jam_buka_lapangan_jam_tutup'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservasi',
            name='jadwal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.jadwal'),
        ),
    ]
