"""
URL Configuration — Project utama katalog_produk.
Mengarahkan semua request ke aplikasi toko.
"""

from django.urls import path, include

urlpatterns = [
    # Semua URL diteruskan ke urls.py milik aplikasi toko
    path('', include('toko.urls')),
]
