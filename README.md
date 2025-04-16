
# Tokopedia Scraper to Excel (Python)

Sebuah script Python sederhana untuk mengambil data produk dari Tokopedia berdasarkan kata kunci dan menyimpannya ke file Excel (.xlsx). Cocok untuk dropshipper, seller online, dan riset pasar.

## 🔧 Fitur
- Input kata kunci (contoh: `mouse gaming`)
- Ambil nama produk, harga, lokasi toko, dan rating
- Simpan hasil ke Excel
- Tanpa login dan ringan dijalankan di laptop biasa

## 🛠 Teknologi
- Python 3.x
- Requests
- BeautifulSoup
- pandas
- openpyxl

## ▶️ Cara Pakai
1. Install dependensi:
   ```
   pip install -r requirements.txt
   ```

2. Jalankan script:
   ```
   python tokopedia_scraper.py
   ```

3. Masukkan kata kunci produk yang ingin dicari.

4. Hasil akan disimpan sebagai file `.xlsx`.

## 📝 Catatan
- Script ini menggunakan scraping HTML biasa. Struktur HTML Tokopedia dapat berubah sewaktu-waktu, sehingga script ini mungkin perlu di-update secara berkala.
