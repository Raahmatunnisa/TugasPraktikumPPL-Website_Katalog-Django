"""
Pengaturan Django untuk project katalog_produk.
"""

from pathlib import Path

# Direktori dasar project
BASE_DIR = Path(__file__).resolve().parent.parent

# Kunci rahasia (jangan gunakan di production)
SECRET_KEY = 'django-insecure-praktikum-katalog-produk-2024'

# Mode debug aktif selama pengembangan
DEBUG = True

ALLOWED_HOSTS = ['*']

# Aplikasi yang terdaftar
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'toko',  # Aplikasi toko kita
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
]

# Konfigurasi URL utama
ROOT_URLCONF = 'katalog_produk.urls'

# Konfigurasi template
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Template dicari di dalam masing-masing app
        'APP_DIRS': True,  # Otomatis cari folder templates/ di tiap app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

# Zona waktu
LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Jakarta'
USE_I18N = True
USE_TZ = True

# File statis (CSS, JavaScript, Gambar)
STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
