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

- Python 3.11 (atau versi Python yang Anda gunakan)
- Django 5.2
- HTML (Template Django)
- SQLite (Default database)

## 📁 Struktur Proyek Singkat

product_manager/ # Folder utama Django project (atau nama root folder Anda)
│ ├── inventaris_project/ # Folder konfigurasi Django project
│ │ ├── settings.py
│ │ ├── urls.py
│ │ └── ...
│ │
│ └── barang/ # Aplikasi produk
│ ├── admin.py # Konfigurasi admin untuk Barang dan Kategori
│ ├── apps.py
│ ├── migrations/
│ ├── models.py # Model Barang dan Kategori
│ ├── templates/
│ │ └── barang/
│ │ └── home.html # Template HTML untuk daftar barang
│ ├── urls.py # Routing internal aplikasi 'barang' (jika ada)
│ ├── views.py # Logic untuk menampilkan daftar barang dan filter
│ └── ...
│
├── db.sqlite3 # Database lokal (biasanya ada di .gitignore)
├── manage.py # Utilitas command-line Django
├── requirements.txt # Library yang dibutuhkan dalam project
└── README.md

## 🧑‍💻 Instalasi dan Menjalankan Proyek

1.  **Clone repository ini**

    ```bash
    git clone https://github.com/NaufalAqil18/inventaris_project.git
    cd inventaris_project
    ```

2.  **Buat dan Aktifkan virtual environment (direkomendasikan)**

    ```bash
    python -m venv env
    source env/bin/activate  # Linux/macOS
    # atau
    # env\Scripts\activate     # Windows
    ```

3.  **Install dependencies**
    Pastikan virtual environment aktif, kemudian install library yang dibutuhkan:

    ```bash
    pip install -r requirements.txt
    ```

4.  **Migrasi database**
    Perintah ini akan membuat tabel-tabel database berdasarkan model Anda:

    ```bash
    python manage.py migrate
    ```

5.  **Buat Superuser (untuk akses Admin)**
    Jika Anda belum memiliki superuser, buat dengan perintah:

    ```bash
    python manage.py createsuperuser
    ```

    Ikuti instruksi di terminal untuk menentukan username, email (opsional), dan password.

6.  **Jalankan server pengembangan**

    ```bash
    python manage.py runserver
    ```

7.  **Buka di browser**
    - Halaman utama pengguna:
      ```
      http://localhost:8000
      ```
    - Halaman Admin:
      ```
      http://localhost:8000/admin
      ```
      Login menggunakan kredensial superuser yang telah Anda buat.

## 🙋‍♂️ Kontribusi

Silakan fork repository ini dan buat pull request jika Anda ingin berkontribusi atau menambahkan fitur lain.
