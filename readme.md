# 🛒 Django Product Inventaris System

Sistem inventaris produk sederhana menggunakan Django. Aplikasi ini memungkinkan pengguna untuk melihat daftar barang, memfilternya berdasarkan kategori, dan bagi admin untuk mengelola data barang serta kategori inventaris.

## 🚀 Fitur

**Fitur Umum Pengguna (Akses Publik):**

- 📋 Lihat Daftar Produk beserta Kategori.
- 🔍 Filter Produk berdasarkan Kategori.

**Fitur Admin (Memerlukan Login):**

- ✅ Tambah, Lihat, Edit, Hapus Produk (Barang).
- ➕ Tambah, Lihat, Edit, Hapus Kategori Produk.
- 🔗 Hubungkan Produk dengan Kategori.
- 📄 Menggunakan Django Model, Form, dan Template (Admin bawaan & kustom).

## 🛠️ Teknologi yang Digunakan

- Python 3.11
- Django 5.2
- HTML (Template Django)
- SQLite (Default database)

## 📁 Struktur Proyek Singkat

```
inventaris_project/  
├── inventaris_project/  
│	├── settings.py  
│	├── urls.py  
│	└── ...  
│  
├── barang/  
│	├── admin.py    
│	├── models.py  
│	├── views.py  
│	├── urls.py  
│	├── templates/  
│	│	├── barang/  
│	│	└── home.html  
│	└── ...  
│  
├── db.sqlite3  
├── manage.py  
├── requirements.txt  
├── kategori_data.json # (Data awal untuk kategori)  
└── barang_data.json # (Data awal untuk barang)  
```
## 🧑‍💻 Instalasi dan Menjalankan Proyek

1. **Clone repository ini**

   ```bash
   git clone https://github.com/NaufalAqil18/inventaris_project.git
   cd inventaris_project
   ```

2. **Buat dan Aktifkan virtual environment (direkomendasikan)**

   ```bash
   python -m venv env
   source env/bin/activate  # Linux/macOS
   # atau
   env\Scripts\activate     # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Migrasi database**

   ```bash
   python manage.py migrate
   ```

5. **Buat Superuser (untuk akses Admin)**

   ```bash
   python manage.py createsuperuser
   ```

6. **Muat Data Awal (Opsional tapi Disarankan)**

   Jika tersedia file `kategori_data.json` dan `barang_data.json`, jalankan:

   ```bash
   python manage.py loaddata kategori_data.json
   python manage.py loaddata barang_data.json
   ```

   Pastikan field yang wajib (seperti `tanggal_ditambahkan`) sudah diisi di dalam file.

7. **Jalankan server pengembangan**

   ```bash
   python manage.py runserver
   ```

8. **Akses dari browser**

   - Halaman utama pengguna:
     ```
     http://localhost:8000
     ```
   - Halaman Admin:

     ```
     http://localhost:8000/admin
     ```

     Login dengan akun superuser yang telah Anda buat.

## 🙋‍♂️ Kontribusi

Silakan fork repository ini dan buat pull request jika Anda ingin berkontribusi atau menambahkan fitur lain.
