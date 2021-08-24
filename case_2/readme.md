Asumsi :
- Website shopee terlihat begitu kompleks karena memang target pasar yang besar, maka harus dapat menyematkan banyak item dalam 1 halaman. Struktur website terlihat rumit dan responsif pada beberapa elemen. Dengan ada nya beberapa encounter masalah yang ada dan dapat ditemukan solusi nya, maka website shopee seharusnya dapat di scraping.

Pembelajaran :
- nama class yang ada pada struktur html pada setiap elemen yang akan di ambil memiliki nama yang unik sehingga memudahkan pelaku scraping dalam mengumpulkan informasi

Tantangan :
- Pada saat pertama kali masuk ke website shopee, maka akan tampil pop up promo dari shopee. Apabila pop up tersebut tampil maka solusi nya adalah cari dan tekan tombol exit, apabila tidak tampil maka lanjutkan scraping
- Setelah dilakukan pencarian maka akan terdapat 60 item, item hanya bisa diambil apabila item tersebut tampil di layar. Solusi dari masalah tersebut adalah dengan memberikan fokus pada item yang sedang di scrap sehingga semua data dapat diambil.
- Pada contoh kasus item konichiwa di haruskan memeriksa 10 halaman akan tetapi total item hanya sampai 3 halaman. Solusi dari masalah tersebut adalah dengan melakukan cek apakah halaman selanjutnya availble. Contoh apabila kita di halaman 1 maka akan dilakukan ceking apakah halaman 2 ada, apabila halaman 2 ada maka lanjutkan ke halaman 2, apabila tidak ada maka hentikan pengambilan data
- pada nama SKU terdapat emoticon yang dapat mengganggu apabila data tersebut kemudian akan dilakukan pemrosesan lain. Solusinya adalah menghapus data non-ascii sehingga data yang deterima bersih dan dapat di proses
- Terdapat range harga pada beberapa item, sehingga dapat membingungkan dalam menghitung GMV. setelah melakukan sedikit riset maka dapat diketahui bahwa total penjualan dari tiap itemlah yang ditampilkan, dan tidak ditampilkan berapa penjualan tiap range harga, sehingga nilai minimum dan maksimum harga memiliki kedudukan yang sama. Dengan kesimpulan tersebut maka akan digunakan nilai minimum dari range harga untuk menghitung GMV, karena apabila menggunakan nilai maksimum maka akan ditemukan gap harga terlalu over dari GMV yang sesungguhnya.
- Terdapat beberapa harga dengan discount, maka akan digunakan harga dengan discount dalam penghitungan GMV.

Pembersihan data :
- Pada harga apabila ada kata "RB" maka akan di rubah dengan angka "000"
- menghilangkan "," pada harga
- menghilangkan kata "terjual" pada jumlah yang terjual