# 🛒 Django Product Management System

Sistem manajemen produk sederhana menggunakan Django. Aplikasi ini memungkinkan pengguna untuk menambahkan, melihat, mengedit, dan menghapus data produk.

## 🚀 Fitur

- ✅ Tambah Produk
- 📋 Lihat Daftar Produk
- ✏️ Edit Produk
- 🗑️ Hapus Produk
- 💬 Pesan notifikasi sukses setiap aksi
- 📄 Menggunakan Django Model, Form, dan Template

## 🛠️ Teknologi yang Digunakan

- Python 3.11
- Django 5.2
- HTML (Template Django)

## 📁 Struktur Proyek Singkat

```
Root
├── product_manager/            # Folder utama Django project
│   ├── product_manager/
│   │   └── ...
│   │
│   ├── products/               # Aplikasi produk
│   │   ├── models.py           # Model produk
│   │   ├── views.py            # Logic tampilan (CRUD)
│   │   ├── urls.py             # Routing internal
│   │   ├── templates/
│   │   │   └── products/       # Template HTML
│   │   │
│   │   ├── db.sqlite3          # Database lokal
│   │   └── manage.py
│   │
│   └── .env.example            # Contoh file variabel lokal
│
├── requirements.txt        # Library yang dibutuhkan dalam project
└── README.md
```

## 🧑‍💻 Instalasi dan Menjalankan Proyek

1. **Clone repository ini**

```bash
git clone https://github.com/NaufalAqil18/Tugas-8-PPL.git
cd Tugas-8-PPL
```

2. **Aktifkan virtual environment (opsional tapi disarankan)**

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Masuk ke directori project**

```bash
cd product_manager
```

5. **Copy local variabel**

Buat secret key yang akan digunakan oleh django.
Secret key dapat anda buat sendiri, ataupun melalui website [ini](https://djecrety.ir/).

Kemudian copy file .env dengan menjalankan code berikut dan tambahkan secret key yang dibuat di file .env.

```bash
cp .env.example .env
```

6. **Migrasi database**

```bash
python manage.py migrate
```

6. **Jalankan server**

```bash
python manage.py runserver
```

7. **Buka di browser**

```
http://localhost:8000
```

---

## 🙋‍♂️ Kontribusi

Silakan fork dan pull request jika ingin berkontribusi atau menambahkan fitur lain.
