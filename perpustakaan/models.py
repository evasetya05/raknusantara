from django.db import models
from django.contrib.auth.models import User


class Perpustakaan(models.Model):
    LAYANAN_CHOICES = [
        ('kurasi', 'Kurasi Buku'),
        ('sewa', 'Sewa Buku'),
        ('jual', 'Jual Buku'),
        ('donasi', 'Donasi Buku'),
        ('tukar', 'Tukar Buku'),
        ('rak', 'Penyusunan Rak'),
        ('katalog', 'Pembuatan Katalog'),
        ('edukasi', 'Edukasi Literasi'),
        ('komunitas', 'Kegiatan Komunitas'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    social_media = models.JSONField(blank=True, null=True)
    alamat = models.TextField(blank=True, null=True)

    # simpan banyak layanan
    layanan = models.JSONField(blank=True, null=True)

    def get_layanan_display(self):
        if not self.layanan:
            return []

        mapping = dict(self.LAYANAN_CHOICES)
        return [mapping.get(kode, kode) for kode in self.layanan]

    def __str__(self):
        return self.name