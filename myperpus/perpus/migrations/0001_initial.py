# Generated by Django 3.2.8 on 2021-10-21 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='daftar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.TextField(max_length=200)),
                ('buku', models.TextField(max_length=200)),
                ('tgl_pinjam', models.IntegerField(max_length=200)),
                ('tgl_kembali', models.IntegerField(max_length=200)),
            ],
        ),
    ]
