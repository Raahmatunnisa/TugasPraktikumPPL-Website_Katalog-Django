#!/usr/bin/env python
"""Utilitas baris perintah Django untuk tugas-tugas administratif."""
import os
import sys


def main():
    """Jalankan tugas administratif."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'katalog_produk.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Tidak dapat mengimpor Django. Pastikan Django sudah terinstal "
            "dan tersedia di variabel lingkungan PYTHONPATH."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
