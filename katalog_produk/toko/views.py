"""
views.py — Kumpulan view (pengontrol) untuk aplikasi toko.
Semua view menggunakan function-based views sesuai ketentuan praktikum.
"""

from django.shortcuts import render
from django.http import Http404
from .data_produk import get_semua_produk, get_produk_by_id


# ─────────────────────────────────────────────
# View: Homepage  →  URL: /
# ─────────────────────────────────────────────
def homepage(request):
    """Menampilkan halaman utama website."""
    konteks = {
        'judul_halaman': 'Selamat Datang',
        'jumlah_produk': len(get_semua_produk()),
    }
    return render(request, 'toko/home.html', konteks)


# ─────────────────────────────────────────────
# View: Daftar Produk  →  URL: /produk/
# ─────────────────────────────────────────────
def daftar_produk(request):
    """Menampilkan semua produk yang tersedia di katalog."""
    semua_produk = get_semua_produk()
    konteks = {
        'judul_halaman': 'Katalog Produk',
        'produk_list': semua_produk,
    }
    return render(request, 'toko/produk.html', konteks)


# ─────────────────────────────────────────────
# View: Detail Produk  →  URL: /produk/<id>/
# ─────────────────────────────────────────────
def detail_produk(request, produk_id):
    """
    Menampilkan detail satu produk berdasarkan ID.
    Akan melempar 404 jika produk tidak ditemukan.
    """
    produk = get_produk_by_id(produk_id)

    # Jika ID tidak ditemukan, tampilkan halaman 404
    if produk is None:
        raise Http404(f"Produk dengan ID {produk_id} tidak ditemukan.")

    konteks = {
        'judul_halaman': produk['nama'],
        'produk': produk,
    }
    return render(request, 'toko/detail_produk.html', konteks)


# ─────────────────────────────────────────────
# View: Kontak  →  URL: /kontak/
# ─────────────────────────────────────────────
def kontak(request):
    """Menampilkan halaman informasi kontak."""
    info_kontak = {
        'nama_toko'  : 'OrbitStore Indonesia',
        'alamat'     : 'Jl. Semangka No.11, Ulee Kareng, Kota Banda Aceh, Aceh 23242',
        'telepon'    : '+62 21 5555-7890',
        'whatsapp'   : '+62 812-3456-7890',
        'email'      : 'cs@orbitstore.id',
        'jam_buka'   : 'Senin – Jumat: 08.00 – 17.00 WIB',
        'instagram'  : '@orbitstore.id',
    }
    konteks = {
        'judul_halaman': 'Hubungi Kami',
        'kontak': info_kontak,
    }
    return render(request, 'toko/kontak.html', konteks)
