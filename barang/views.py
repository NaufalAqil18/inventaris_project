from django.shortcuts import render
from .models import Barang

def home(request):
    daftar_barang = Barang.objects.all()
    return render(request, 'barang/home.html', {'barang': daftar_barang})
