# 🛒 Django Product Inventaris System

Sistem inventaris produk sederhana menggunakan Django. Aplikasi ini memungkinkan pengguna untuk menambahkan, melihat, mengedit, dan menghapus data barang inventaris.

## 🚀 Fitur

- ✅ Tambah Produk
- 📋 Lihat Daftar Produk
- ✏️ Edit Produk
- 🗑️ Hapus Produk
- 📄 Menggunakan Django Model, Form, dan Template

## 🛠️ Teknologi yang Digunakan

- Python 3.11
- Django 5.2
- HTML (Template Django)

## 📁 Struktur Proyek Singkat

```
product_manager/                # Folder utama Django project
│   ├── inventaris_project/
│   │   └── ...
│   │
│   └── barang/                 # Aplikasi produk
│       ├── models.py           # Model produk
│       ├── views.py            # Logic tampilan (CRUD)
│       ├── urls.py             # Routing internal
│       ├── templates/
│       │   └── home/           # Template HTML
│       │
│       ├── db.sqlite3          # Database lokal
│       └── manage.py
│
├── requirements.txt            # Library yang dibutuhkan dalam project
└── README.md
```

## 🧑‍💻 Instalasi dan Menjalankan Proyek

1. **Clone repository ini**

```bash
git clone https://github.com/NaufalAqil18/inventaris_project.git
cd inventaris_project
```

2. **Aktifkan virtual environment (opsional)**

```bash
python -m venv env
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows
```

3. **Install dependencies**

Install library django agar server dapat dijalankan

```bash
pip install -r requirements.txt
```

4. **Migrasi database**

Populasi database dengan migrate

```bash
python manage.py migrate
```

5. **Jalankan server**

Jalankan server dengan menjalankan perintah berikut:

```bash
python manage.py runserver
```

6. **Buka di browser**

```bash
http://localhost:8000
```

untuk admin page, silahkan buka halaman dibawah, dengan kredensial berikut

```bash
http://localhost:8000/admin
```

```
# username: admin
# password: admin123
```

---

## 🙋‍♂️ Kontribusi

Silakan fork dan pull request jika ingin berkontribusi atau menambahkan fitur lain.
