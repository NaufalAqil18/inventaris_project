from django.shortcuts import render
from .models import Barang, Kategori # Impor Kategori

def home(request):
    kategori_filter_id = request.GET.get('kategori_id') # Ambil ID kategori dari parameter URL
    semua_kategori = Kategori.objects.all() # Ambil semua objek Kategori

    if kategori_filter_id:
        try:
            # Filter barang berdasarkan ID kategori yang dipilih
            daftar_barang = Barang.objects.filter(kategori__id=kategori_filter_id)
            kategori_filter_id = int(kategori_filter_id)
        except ValueError:
            # Jika kategori_id tidak valid, tampilkan semua barang
            daftar_barang = Barang.objects.all()
            kategori_filter_id = None
    else:
        daftar_barang = Barang.objects.all() # Jika tidak ada filter, tampilkan semua barang

    context = {
        'barang': daftar_barang,
        'kategori_tersedia': semua_kategori, # Kirim daftar kategori ke template
        'kategori_dipilih_id': kategori_filter_id, # Kirim ID kategori yang dipilih
    }
    return render(request, 'barang/home.html', context)