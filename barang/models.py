from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=50, unique=True, verbose_name="Nama Kategori")
    deskripsi = models.TextField(blank=True, null=True, verbose_name="Deskripsi Kategori")

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Kategori" # Nama yang akan tampil di admin

class Barang(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    jumlah = models.PositiveIntegerField()
    lokasi = models.CharField(max_length=100)
    tanggal_ditambahkan = models.DateTimeField(auto_now_add=True)
    # Tambahkan ForeignKey ke Kategori
    # models.SET_NULL: Jika kategori dihapus, field kategori pada barang akan di-set NULL.
    # null=True: Memungkinkan field ini kosong di database.
    # blank=True: Memungkinkan field ini kosong di form Django.
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, blank=True, related_name='barang')

    def __str__(self):
        return self.nama