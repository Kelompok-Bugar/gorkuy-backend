# Generated by Django 4.1.3 on 2022-12-04 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_rekening_remove_pembayaran_jumlah'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservasi',
            name='totalHarga',
        ),
        migrations.AlterField(
            model_name='reservasi',
            name='lapangan',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='database.lapangan'),
        ),
    ]
