"""
urls.py — Routing URL untuk aplikasi toko.
Mendefinisikan semua pola URL yang tersedia di website.
"""

from django.urls import path
from . import views

# Namespace aplikasi (berguna untuk reverse URL)
app_name = 'toko'

urlpatterns = [
    # Halaman utama  →  /
    path('', views.homepage, name='homepage'),

    # Daftar semua produk  →  /produk/
    path('produk/', views.daftar_produk, name='daftar_produk'),

    # Detail satu produk  →  /produk/<id>/
    # produk_id harus berupa angka bulat (int)
    path('produk/<int:produk_id>/', views.detail_produk, name='detail_produk'),

    # Halaman kontak  →  /kontak/
    path('kontak/', views.kontak, name='kontak'),
]
