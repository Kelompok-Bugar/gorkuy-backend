# Generated by Django 4.1.3 on 2022-12-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_alter_reservasi_lapangan_alter_reservasi_penyewa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservasi',
            name='totalHarga',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]