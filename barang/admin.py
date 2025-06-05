from django.contrib import admin
from .models import Barang, Kategori # Impor Kategori

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ('nama', 'deskripsi')
    search_fields = ('nama',)

@admin.register(Barang)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kategori', 'jumlah', 'lokasi', 'deskripsi') # Tambahkan 'kategori'
    search_fields = ('nama', 'deskripsi')
    list_filter = ('lokasi', 'kategori') # Tambahkan 'kategori' untuk filter
    list_editable = ('jumlah', 'lokasi', 'kategori') # Tambahkan 'kategori' agar bisa diedit langsung dari list
    autocomplete_fields = ['kategori'] # Untuk pilihan kategori yang lebih baik jika kategori banyak

'''
    username : admin
    email : admin@gmail.com
    pass : admin123
'''