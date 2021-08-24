Alat :
- Menggunakan Selenium, karena akan memudahkan dalam melakukan debugging. Saat terjadi error maka tampilan web akan berhenti dimana terjadi error, tidak seperti saat menggunakan BeautifulSoup4 saat error maka pelaku scraping perlu membuka web secara manual (Membuka browser dan memasukkan link sendiri) saat hendak cek struktur html
- Menggunakan Pandas untuk membuka list url dan menyimpan hasil ke csv

Asumsi :
- Website terlihat simple dalam penampilan informasi dan style sederhana, pengambilan informasi (Scraping) dalam website ini dapat dikatakan cukup mudah karena informasi yang di inginkan sudah tersedia dan ditampilkan dengan struktur html yang tidak rumit.

Pembelajaran :
- Hampir semua elemen yang akan diambil data nya dapat menggunakan metode copy xpath karena tampilan website yang sederhana.

Tantangan :
- Beberapa kali muncul alert "Pilih lokasi anda", dapat diatasi dengan mendeteksi tombol exit pada pojok kanan alert melalui xpath. Apabila terdapat tombol exit maka di klik, apabila tidak maka lanjutkan scraping.
- Informasi mengenai stock antara available dan out of stock memiliki struktur html yang berbeda, dapat diatasi dengan mendeteksi tulisan out of stock melalui xpath, apabila tidak ada tulisan tersebut maka stock available.
- Harga SKU memiliki id yang unik, sehingga tidak bisa asal copy xpath. Dapat diatasi dengan deteksi kontainer informasi produk secara keseluruhan lalu dari situ dapat di deteksi harga SKU dengan deteksi element span yang memiliki class "price-wrapper". Setelah mendapat elemen maka untuk mendapatkan hasil yang bersih dapat di ambil atribute "data-price-amount".