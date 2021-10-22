from django.db import models
# from django.db.models.base import Model
# from django.db.models.fields import CharField, IntegerField
# Create your models here.
class pinjam(models.Model):
    nmr_anggota = models.IntegerField()
    nama = models.TextField(max_length=200)
    buku = models.TextField(max_length=200)
    jml_buku = models.IntegerField()
    tgl_pinjam = models.DateField(blank=True, null=True)
    tgl_kembali = models.DateField(blank=True, null=True)