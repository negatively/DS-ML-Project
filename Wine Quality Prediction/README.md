# Laporan Proyek Machine Learning Prediksi Wines
## Domain Proyek
Domain proyek yang penulis pilih untuk proyek machine learning kali ini adalah food and beverage dengan judul proyek "Prediksi Kualitas Red Wine menggunakan Random Forest"

### Latar Belakang
Kualitas wine merupakan suatu hal yang sangat penting, karena mengkonsumsi wine berkualitas rendah akan berdampak buruk bagi kesehatan manusia. Industri wine adalah sektor besar di mana mereka akan menipu orang dalam kualitas wine. Setiap jenis wine yang berbeda akan memiliki konsentrasi zat kimia yang berbeda juga. Untuk menjaga kualitas dengan biaya rendah, penting untuk mengetahui kandungan konsentrasi zat kimia yang digunakan dalam berbagai jenis wine [1]. Pendekatan manual untuk mengidentifikasi kualitas wine membutuhkan waktu yang lama dan memiliki tingkat akurasi yang rendah [2]. Dan dengan menganalisa kandungan konsentrasi zat kimia dapat kita peroleh cara untuk membedakan kualitas wine.

## Business Understanding
### Rumusan Masalah
Berdasarkan uraian latar belakang yang telah dijelaskan diatas, maka dapat diperoleh rumusan masalah :

*   Bagaimana kinerja _Random Forest_ untuk prediksi kualitas wine?
* Fitur apa yang paling berpengaruh pada penentuan kualitas red wine?

### Tujuan
Tujuan dari proyek yang dikerjakan adalah Membuat sistem prediksi kualitas wine yang memiliki tingkat akurasi > 80% untuk membantu orang dalam menentukan kualitas wine.

### Solusi Permasalahan
Solusi untuk menyelesaikan permasalahan berdasarkan tujuan proyek adalah :
* Melakukan pengolahan data pada proses pra-pemrosesan untuk meningkatkan akurasi prediksi.
* Menggunakan algoritma pemodelan Random Forest sebagai model baseline. Pemilihan algoritma tersebut dipilih karena cocok untuk kasus klasifikasi dam mudah udah digunakan.
* Model baseline yang sudah dibuat kemudian di kembangkan dengan cara melakukan tuning hyperparameter. Pengaturan tuning hyperparameter yang dilakukan menggunakan `GridSearchCV`. 
## Data Understanding
Data yang digunakan untuk proyek kali ini adalah Red Wine Dataset yang diunduh dari [dataset Kaggle](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009). Dataset tersebut memiliki jumlah data sebanyak 1599 baris dengan 11 fitur dan 1 target. Fitur yang dimaksud adalah _fixed acidity_, _volatile acidity_, _citric acid_, _residual sugar_, _chlorides_, _free sulfur dioxide_, _total sulfur dioxide_, _density_, _pH_, _sulphates_, dan _alcohol_ yang bertipe data numerik. Sedangkan _quality_ adalah target yang juga bertipe data numerik. Untuk penjelasan tentang variabel-variabel pada dataset _Red Wine_ dapat dilihat pada poin-poin berikut :
* `fixed acidity` :  kandungan asam yang bersifat sudah tentu
* `volatile acidity` :  kandungan asam yang bersifat _volatile_
* `citric acid` : kandungan asam sitrat
* `residual sugar` : jumlah kandungan gula residual karena proses fermentasi
* `chlorides` :  kandungan garam pada wines
* `free sulfur dioxide` : kandungan SO2 dalam bentuk kesetimbangan antara molekul SO2 (sebagai gas terlarut) dan ion bisulfit
* `total sulfur dioxide` : jumlah keseluruhan S02
* `density` :  tingkat kerapatan cairan
* `pH` :  menggambarkan seberapa asam atau basa anggur dalam skala dari 0 (sangat asam) hingga 14 (sangat basa)
* `sulphates` : kadar aditif wines yang dapat berkontribusi pada tingkat gas sulfur dioksida (S02)
* `alcohol` : persentase kandungan alkohol pada wines
* `quality` :  variabel output berdasarkan data sensorik dengan skor dari 0 sampai 10

Kemudian terdapat juga visualisasi tentang korelasi antar kolomnya. 
![Correlation](https://github.com/negatively/DS-ML-Project/blob/main/Wine%20Quality%20Prediction/Image/correlation.png)


## Data Preparation
Tahap berikutnya adalah _data preparation_, tahap dimana data akan diolah sehingga sudah siap untuk proses pemodelan. Dan berikut adalah tahapan dalam _data preparation_ :
* Mengapus data yang memiliki outlier di lebih dari 3 fitur. _Outliers_ sendiri dapat mempengaruhi performa dari model 
* Mengelompokkan data quality menjadi `good` dan `not good`, dimana data yang memiliki label `good` merupakan red wine yang baik untuk kesehatan. Data yang memiliki nilai quality 0 sampai 6 merupakan wine dengan kualitas `not good`. Sedangkan data yang memiliki nilai 7 sampai 10 merupakan wine dengan kualitas `good`.
* Tidak mengikutkan fitur _residual sugar_, _free sulfur dioxide_, dan _pH_ karena memiliki tingakt korelasi dibawah 0.1 terhadap _quality_
* Membagi dataset menjadi data _train_ dan data _test_ dengan rasio 80% untuk data _train_ dan 20% untuk data _test_. Tujuan dilakukan pembagian adalah supaya dapat menguji performa model. Dimaana data _train_ digunakan untuk melatih model, sedangkan data _test__ merupakan data yang digunakan untuk menguji model setelah melalui pelatihan data. 
* Standarisasi pada semua fitur dataset. Standarisasi yang dilakukan adalah menggunakan teknik [StandardScaler](https://scikit-learn.org/0.24/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler), dimana data akan dikurangi dengan nilai rata-rata kemudian dibagi dengan standar deviasi, sehingga dataset akan memiliki standar deviasi sebesar 1 dan rata-rata sama dengan 0.

## Modelling
Setelah dataset diolah, maka proses selanjutnya adalah pemodelan. Tahap yang dilakukan pada proses ini diantaranya adalah pembuatan model baseline dan tuning hyperparameter dengan GridSearchCV.
*   Model baseline
    
    Pada langkah ini dibuat sebuah model Random Forest dengan library scikit-learn RandomForestClassifier. Dalam pemodelan ini model dibuat tanpa parameter tambahan. Di langkah ini model baseline yang sudah dibuat kemudian dikembangkan kinerjanya. Untuk meningkatkan kinerja model maka dilakukan pencarian hyperparameter yang optimal untuk model dengan GridSearchCV. Setelah ditemukan hyperparameter terbaik dari proses GridSearchCV, kemudian diterapkan ke model baseline

*   Tuning Hyperparameter
    
    Di langkah ini model baseline yang sudah dibuat kemudian dikembangkan kinerjanya. Untuk meningkatkan kinerja model maka dilakukan pencarian hyperparameter yang optimal untuk model dengan GridSearchCV. Setelah ditemukan hyperparameter terbaik dari proses GridSearchCV, kemudian diterapkan ke model baseline
    

## Evaluation
Model yang telah dibuat kemudian dilakukan evaluasi. Karena model merupakan tipe klasifikasi, maka evaluasinya akan digunakan metriks akurasi, _f1-score_, _precision_, dan _recall_.
* Akurasi

    Akurasi merupakan metrik untuk menghitung nilai ketepatan model dalam memprediksi data dengan data yang sebenarnya. Akurasi dapat dihitung dengan rumus diatas. 
* F1-score
* Precision
* Recall

## Referensi
* [1] V. Preedy, and M. L. R. Mendez, “Wine Applications with Electronic Noses,” in Electronic Noses and Tongues in Food Science, Cambridge, MA, USA: Academic Press, 2016, pp. 137-151.
* P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547-553, 2009.



