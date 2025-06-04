from django.contrib import admin
from .models import Barang

@admin.register(Barang)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'deskripsi', 'jumlah', 'lokasi')
    search_fields = ('nama','deskripsi')
    list_filter = ('lokasi',)
    list_editable = ('jumlah', 'lokasi')


'''
    username : admin
    email : admin@gmail.com
    pass : admin123
'''