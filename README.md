# 📦 Katalog Produk — Praktikum PPL


**Nama**: Rahmatun Nisa  
**NIM**: 2308107010016  
**Framework**: Django  

---

## 📝 Penjelasan Singkat Program

Website **TechStore Indonesia** adalah aplikasi katalog produk sederhana berbasis Django yang menampilkan daftar produk teknologi tanpa menggunakan database. Seluruh data produk di-*hardcode* langsung di dalam file Python (`data_produk.py`).

### Fitur Utama

| Halaman | URL | Keterangan |
|---------|-----|------------|
| Homepage | `/` | Halaman selamat datang dengan ringkasan toko |
| Daftar Produk | `/produk/` | Menampilkan semua produk dalam format kartu |
| Detail Produk | `/produk/<id>/` | Menampilkan detail lengkap satu produk |
| Kontak | `/kontak/` | Informasi kontak dan jam operasional toko |

### Struktur Teknis

- **Function-based views** — semua logika halaman ditulis sebagai fungsi Python biasa
- **Template inheritance** — `base.html` sebagai template induk, halaman lain meng-*extend*-nya
- **Tanpa database** — data produk disimpan sebagai list of dictionary di `data_produk.py`
- **CSS inline** — styling sederhana tanpa framework eksternal

---

## 🗂️ Struktur Folder

```
katalog_produk/
├── manage.py
├── katalog_produk/          ← Konfigurasi project
│   ├── __init__.py
│   ├── settings.py
│   └── urls.py
└── toko/                    ← Aplikasi utama
    ├── __init__.py
    ├── data_produk.py       ← Data produk hardcoded
    ├── views.py             ← Function-based views
    ├── urls.py              ← Routing URL
    └── templates/
        └── toko/
            ├── base.html
            ├── home.html
            ├── produk.html
            ├── detail_produk.html
            └── kontak.html
```

---

## ▶️ Cara Menjalankan Project

### 1. Pastikan Python & pip terinstal
```bash
python --version   # Minimal Python 3.10
```

### 2. Install Django
```bash
pip install django
```

### 3. Masuk ke folder project
```bash
cd katalog_produk
```

### 4. Jalankan server
```bash
python manage.py runserver
```

### 5. Buka di browser
```
http://127.0.0.1:8000/
```

---

## 🌐 Daftar URL

| URL | Keterangan |
|-----|------------|
| `http://127.0.0.1:8000/` | Homepage |
| `http://127.0.0.1:8000/produk/` | Daftar Produk |
| `http://127.0.0.1:8000/produk/1/` | Detail Produk ID 1 |
| `http://127.0.0.1:8000/produk/2/` | Detail Produk ID 2 |
| `http://127.0.0.1:8000/kontak/` | Halaman Kontak |

---

## 🛍️ Data Produk (Hardcoded)

| ID | Nama | Harga |
|----|------|-------|
| 1 | Laptop UltraBook Pro | Rp 12.500.000 |
| 2 | Headphone Wireless Noise-Cancelling | Rp 1.850.000 |
| 3 | Mechanical Keyboard TKL | Rp 850.000 |
| 4 | Mouse Ergonomis Silent | Rp 320.000 |
| 5 | Webcam HD 1080p | Rp 475.000 |
