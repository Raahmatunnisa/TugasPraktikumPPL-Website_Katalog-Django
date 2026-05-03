"""
data_produk.py — Data produk yang di-hardcode (tanpa database).
Berisi daftar produk yang akan ditampilkan di website katalog.
"""

# Daftar produk — setiap produk berupa dictionary dengan field:
# id, nama, deskripsi, harga, emoji (ikon dekoratif)
DAFTAR_PRODUK = [
    {
        'id': 1,
        'nama': 'Laptop UltraBook Pro',
        'deskripsi': (
            'Laptop tipis dan ringan dengan prosesor Intel Core i7 generasi terbaru. '
            'Dilengkapi RAM 16GB, SSD 512GB, dan layar IPS 14 inci resolusi Full HD. '
            'Baterai tahan hingga 12 jam pemakaian normal. Cocok untuk mahasiswa dan profesional.'
        ),
        'harga': 12_500_000,
        'emoji': '💻',
        'kategori': 'Elektronik',
    },
    {
        'id': 2,
        'nama': 'Headphone Wireless Noise-Cancelling',
        'deskripsi': (
            'Headphone over-ear dengan teknologi Active Noise Cancellation (ANC) terdepan. '
            'Kualitas suara Hi-Fi dengan driver 40mm. Koneksi Bluetooth 5.0, baterai 30 jam. '
            'Desain foldable dan nyaman dipakai lama. Dilengkapi mikrofon built-in.'
        ),
        'harga': 1_850_000,
        'emoji': '🎧',
        'kategori': 'Elektronik',
    },
    {
        'id': 3,
        'nama': 'Mechanical Keyboard TKL',
        'deskripsi': (
            'Keyboard mekanikal tenkeyless (80%) dengan switch Cherry MX Red. '
            'Backlight RGB per-key yang bisa dikustomisasi. Build quality premium dengan '
            'frame aluminium. Kompatibel dengan Windows, macOS, dan Linux via USB-C.'
        ),
        'harga': 850_000,
        'emoji': '⌨️',
        'kategori': 'Aksesori',
    },
    {
        'id': 4,
        'nama': 'Mouse Ergonomis Silent',
        'deskripsi': (
            'Mouse wireless ergonomis dengan desain vertikal yang mengurangi kelelahan pergelangan tangan. '
            'Sensor optik 1600 DPI, tombol klik senyap (silent click), baterai AAA tahan 18 bulan. '
            'Cocok untuk pengguna yang bekerja berjam-jam di depan komputer.'
        ),
        'harga': 320_000,
        'emoji': '🖱️',
        'kategori': 'Aksesori',
    },
    {
        'id': 5,
        'nama': 'Webcam HD 1080p',
        'deskripsi': (
            'Webcam resolusi Full HD 1080p dengan autofocus otomatis dan koreksi cahaya rendah. '
            'Mikrofon stereo bawaan dengan peredam kebisingan. Plug-and-play via USB, '
            'tidak perlu instalasi driver. Ideal untuk video call, streaming, dan kuliah online.'
        ),
        'harga': 475_000,
        'emoji': '📷',
        'kategori': 'Elektronik',
    },
]


def get_semua_produk():
    """Mengembalikan seluruh daftar produk."""
    return DAFTAR_PRODUK


def get_produk_by_id(produk_id):
    """
    Mencari dan mengembalikan produk berdasarkan ID.
    Mengembalikan None jika produk tidak ditemukan.
    """
    for produk in DAFTAR_PRODUK:
        if produk['id'] == produk_id:
            return produk
    return None
