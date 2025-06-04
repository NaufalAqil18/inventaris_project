from django.db import models

class Barang(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    jumlah = models.PositiveIntegerField()
    lokasi = models.CharField(max_length=100)
    tanggal_ditambahkan = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama