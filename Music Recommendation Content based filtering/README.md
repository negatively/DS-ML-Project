# Laporan Proyek Sistem Rekomendasi Musik Spotify
## Ulasan Proyek
![spotify](https://user-images.githubusercontent.com/61934759/137764151-d27729b5-7145-4df8-97e2-168e7bbb0caf.png)
Proyek berupa sistem rekomendasi musik yang ditunjukkan bagi pengguna aplikasi Spotify. Sistem rekomendasi musik ini menggunakan pendekatan _content-based filtering_. Sistem rekomendasi adalah algoritme yang digunakan untuk membuat saran yang akurat berdasarkan preferensi atau kebutuhan pengguna `[1]`. _Content-based filtering_ melakukan rekomendasi dengan mempelajari kesamaan item konten yang telah dipilih pengguna `[2]`.


Musik telah menjadi salah satu seni yang disenangi oleh masyarakat di seluruh dunia. Musik datang dalam berbagai genre, seperti rock, klasik, tradisional, pop, dan banyak lagi. Evolusi teknologi dalam musik saat ini memudahkan pecinta musik untuk mengakses lagu dari aplikasi yang tersedia. Salah satunya adalah aplikasi Spotify. Spotify adalah aplikasi pemutar musik yang menyediakan berbagai lagu dari berbagai kategori dan popularitas. Pengguna dapat mendengarkan artis dan genre favorit mereka dengan aplikasi Spotify ini. Karena banyaknya musik yang terdapat pada Spotify terkadang pengguna bingung untuk memilih yang cocok dengan seleranya. Dan jika hanya mendengarkan lagu yang sama terus-menerus akan timbul rasa bosan. Oleh karena itu dibuatlah sistem rekomendasi ini untuk merekomendasikan pengguna terkait lagu yang sesuai dengan seleranya.

## Business Understanding
### Rumusan Masalah
Berdasarkan uraian dari ulasan proyek yang telah dijelaskan sebelumnya, maka dapat diperoleh rumusan masalah :
* Bagaimana penggunaan _content-based filtering_ untuk sistem rekomendasi musik?

### Tujuan
Tujuan dari proyek yang dikerjakan adalah :
* Membuat sistem rekomendasi dengan menggunakan _content-based filtering_
* Melakukan penerapan metriks presisi untuk melihat performa dari rekomendasi sistem

### Solution Approach
Solusi untuk menyelesaikan permasalahan berdasarkan tujuan proyek adalah :
* Melakukan pengolahan data pada tahap _data preparation_ untuk meningkatkan presisi rekomendasi
* Menggunakan pendekatan _cosine similarity_ untuk rekomendasi berdasarkan content-based filtering

## Data Understanding
Data yang digunakan untuk proyek kali ini adalah 19,000 Spotify Song yang diunduh dari [Dataset Kaggle](https://www.kaggle.com/edalrami/19000-spotify-songs/code). Dataset tersebut memiliki dua buah file berformat csv, yaitu _song_data.csv_ dan _song_info.csv_. _song_data.csv_ berisi informasi yang berkaitan tentang atribut audio lagu. Sedangkan _song_info.csv_ berisi informasi yang berkaitan tentang metadata lagu. Untuk proyek kali ini kita hanya akan menggunakan _song_info.csv__. _song_info.csv_ memiliki jumlah data sebanyak 18835 baris dengan 4 kolom, kolom yang dimaksud adalah `song_name`, `artist_name`, `album_names`, dan `playlist` yang bertipe sebagai object. Untuk penjelasan tentang variabel-variabel kolom tersebut, dapat dilihat pada poin-poin berikut :
* `song_name` : Judul lagu yang tertampil
* `artist_name` : Nama penyanyi yang menyanyikan lagu tersebut
* `album_names` : Nama album dimana lagu tersebut termasuk sebagai koleksinya, album sendiri adalah koleksi lagu dari suatu penyanyi
* `playlist` : Kumpulan lagu yang memiliki suatu kesamaan

Dari hasil eksplorasi unique value untuk tiap variabel kolom,hasilnya adalah sebagai berikut :
* Pada kolom `song_name` terdapat 13070 nama lagu
* Pada kolom `artist_name` terdapat 7564 penyanyi
* Pada kolom `album_names` terdapat 12014 judul album
* Pada kolom `playlist` terdapat 300 nama playlist

Kemudian berikut adalah visualiasasi terkait jumlah penyayi dan playlist dengan lagu terbanyak dalam dataset ini
![top artis](https://user-images.githubusercontent.com/61934759/138030863-511530f5-2203-4861-9b4a-7eb0756fcaed.JPG)
![top playlist](https://user-images.githubusercontent.com/61934759/138030860-7ecb2452-7fd2-4029-ae6a-edfc7de1a0c1.JPG)


## Data Preparation
Tahap berikutnya adalah _data preparation_, tahap dimana data akan diolah sehingga sudah siap untuk proses pemodelan. Dan berikut adalah tahapan dalam tahap _data preparation_:
* Membuang data duplikasi yang memiliki kesamaan pada kolom `song_name` dan  `artist_name`. Tujuannya supaya tidak muncul suatu data sebanyak 2 kali pada proses rekomendasi nanti. Proses penghilangan data duplikasi ini adalah dengan perintah _drop_duplicates_ dari library pandas.
* Membuat fitur baru bernama `info` dengan cara menggabungkan kolom `artist_name`, `album_names`, dan `playlist`. Hal tersebut dilakukan untuk memudahkan proses TF-IDF, karena fitur `info` telah mencakup ketiga fitur kolom.

## Pemodelan dan Hasil
Setelah data telah diolah, maka proses selanjutnya adalah pemodelan

* TF-IDF 
    Secara sederhana TF merupakan frekuensi kemunculan kata dalam suatu dokumen. IDF merupakan sebuah perhitungan dari bagaimana kata didistribusikan secara luas pada koleksi dokumen yang bersangkutan. Pada projek ini TF-IDF digunakan pada sistem rekomendasi untuk menemukan representasi fitur penting dari setiap kategori masakan. Untuk melakukan proses TF-IDF ini digunakan fungsi _TfidfVectorizer_ dari sklearn.

* Cosine similarity    
    _Cosine similarity_ adalah metrik yang digunakan untuk mengukur tingkat kesamaan suatu dokumen terlepas dari ukurannya. Dan secara matematis, _cosine similarity_ mengukur kosinus sudut antara dua vektor yang diproyeksikan dalam ruang multidimensi. _Cosine similarity_ memiliki keuntungan apabila dua dokumen serupa terpisah oleh _euclidean distance_ karena ukuran dokumen, kemungkinan mereka masih berorientasi ada. Dalam proses ini _cosine similarity_ dipanggil dengan fungsi _cosine_similarity_ dari sklearn. Input fungsi _cosine_similarity_ adalah matrix hasil dari proses TF-IDF, yang kemudian menghasilkan output berupa array tingkat kesamaan.

* Membuat Fungsi _song_recommendations_    
    Fungsi tersebut digunakan untuk memberikan rekomendasi berdasarkan sebuah nama lagu. Pada fungsi tersebut akan dilakukan pencarian kolom  yang sama dengan nama lagu yang dimasukkan pada dataframe hasil _cosine similarity_. Setelah itu diurutkan berdasarkan nilai _cosine similarity_ tertinggi, kemudian dilakukan _drop_ nama lagu yang dijadikan acuan agar tidak muncul dalam daftar rekomendasi. Kemudian outputnya berupa 5 lagu yang memiliki cosine similarity tertinggi. Hasil dari fungsi ini dapat dilihat pada gambar berikut :

    ![hasil](https://user-images.githubusercontent.com/61934759/138030673-9e6c0057-c38d-4049-bfbe-44a29953680a.JPG)

## Evaluasi
Sistem rekomendasi yang telah dibuat kemudian dilakukan evaluasi. Untuk mengukur kinerja sistem rekomendasi digunakan matriks presisi. Presisi merupakan banyaknya item rekomendasi yang relevan dibagi dengan banyaknya item yang direkomendasikan. Rumus dari metriks presisi adalah sebagai berikut :
![presisi](https://user-images.githubusercontent.com/61934759/138005224-8c8be6fd-58d8-4bc6-978f-d7ee5ce9c3e8.JPG)

Dan dari perhitungan metriks presisi didapatkan nilai 80%, untuk lebih jelasnya bisa dilihat pada gambar berikut,
![presisi rekomendasi](https://user-images.githubusercontent.com/61934759/138032733-58bcde90-a8b4-4ec1-94ef-ffc2e4169e7b.JPG)


## Referensi
* `[1]` P. Jomsri, S. Sanguansintukul, and W. Choochaiwattana, “A framework for tag-based research paper recommender system: An ir approach,” in 2010 IEEE 24th International Conference on Advanced Information Networking and Applications Workshops, April 2010, pp. 103–108
* `[2]` M. Hassan and M. Hamada, “Improving prediction accuracy of multicriteria recommender systems using adaptive genetic algorithms,” in 2017 Intelligent Systems Conference (IntelliSys), Sept 2017, pp. 326–330.




