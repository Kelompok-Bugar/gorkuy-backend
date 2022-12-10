# Generated by Django 4.1.3 on 2022-12-03 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rekening',
            fields=[
                ('penyewa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='database.penyewa')),
                ('saldo', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='pembayaran',
            name='jumlah',
        ),
    ]