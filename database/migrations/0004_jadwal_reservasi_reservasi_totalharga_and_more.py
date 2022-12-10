# Generated by Django 4.1.3 on 2022-12-10 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_remove_reservasi_totalharga_alter_reservasi_lapangan'),
    ]

    operations = [
        migrations.AddField(
            model_name='jadwal',
            name='reservasi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.reservasi'),
        ),
        migrations.AddField(
            model_name='reservasi',
            name='totalHarga',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='reservasi',
            name='lapangan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.lapangan'),
        ),
        migrations.AlterField(
            model_name='reservasi',
            name='penyewa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='database.penyewa'),
        ),
    ]