# Laporan Proyek Machine Learning Prediksi Wines
## Domain Proyek
Domain proyek yang penulis pilih untuk proyek machine learning kali ini adalah food and beverage dengan judul proyek "Prediksi Kualitas Red Wine menggunakan Random Forest"

### Latar Belakang
Kualitas wine merupakan suatu hal yang sangat penting, karena mengkonsumsi wine berkualitas rendah akan berdampak buruk bagi kesehatan manusia. Industri wine adalah sektor besar di mana mereka akan menipu orang dalam kualitas wine. Setiap jenis wine yang berbeda akan memiliki konsentrasi zat kimia yang berbeda juga. Untuk menjaga kualitas dengan biaya rendah, penting untuk mengetahui kandungan konsentrasi zat kimia yang digunakan dalam berbagai jenis wine [1]. Pendekatan manual untuk mengidentifikasi kualitas wine membutuhkan waktu yang lama dan memiliki tingkat akurasi yang rendah [2]. Dan dengan menganalisa kandungan konsentrasi zat kimia dapat kita peroleh cara untuk membedakan kualitas wine.

## Business Understanding
### Rumusan Masalah
Berdasarkan uraian latar belakang yang telah dijelaskan diatas, maka dapat diperoleh rumusan masalah :

* Bagaimana kinerja _Random Forest_ untuk prediksi kualitas wine?
* Fitur apa yang paling berpengaruh pada penentuan kualitas red wine?

### Tujuan
Tujuan dari proyek yang dikerjakan adalah :
* Membuat model prediksi dengan algortima _Random Forest_
* Melakukan penerapan metrics akurasi, f1-score, precision, dan recall untuk melihat performa prediksi dari model.
* Mencari tingkat keberpengaruhan fitur-fitur pada model berdasarkan hasil visualisasi.

### Solusi Permasalahan
Solusi untuk menyelesaikan permasalahan berdasarkan tujuan proyek adalah :
* Melakukan pengolahan data pada proses pra-pemrosesan untuk meningkatkan akurasi prediksi.
* Menggunakan algoritma pemodelan Random Forest sebagai model baseline. Pemilihan algoritma tersebut dipilih karena cocok untuk kasus klasifikasi dam mudah udah digunakan.
* Model baseline yang sudah dibuat kemudian di kembangkan dengan cara melakukan tuning hyperparameter. Pengaturan tuning hyperparameter yang dilakukan menggunakan `GridSearchCV`. 
* Menerapkan metrics akurasi, f1-score, precision, dan recall pada model
* Mencari _feature importances_ pada model yang telha dibuat untuk mengetahui pengaruh dari suatu fitur pada prediksi model.

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
![correlation](https://user-images.githubusercontent.com/61934759/136343461-dbfc961e-1cc9-41a8-9d32-db4e0b30f56a.png)

Berdasarkan plot heatmap korelasi diatas, fitur yang memiliki korelasi diantara -0.1 sampai 0.1 dengan fitur quality adalah residual sugar, free sulfur dioxide, dan pH. Oleh karena itu fitur tersebut nantinya dapat di drop


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
    
    Pada langkah ini dibuat sebuah model Random Forest dengan library scikit-learn RandomForestClassifier. Dalam pemodelan ini model dibuat tanpa parameter tambahan. 

*   Tuning Hyperparameter
    
    Di langkah ini model baseline yang sudah dibuat kemudian dikembangkan kinerjanya. Untuk meningkatkan kinerja model maka dilakukan pencarian hyperparameter yang optimal untuk model dengan GridSearchCV. Setelah ditemukan hyperparameter terbaik dari proses GridSearchCV, kemudian diterapkan ke model baseline
    

## Evaluation
Model yang telah dibuat kemudian dilakukan evaluasi. Karena model merupakan tipe klasifikasi, maka evaluasinya akan digunakan metriks akurasi, _f1-score_, _precision_, dan _recall_.
* Akurasi

    ![accuracy](https://user-images.githubusercontent.com/61934759/136345298-cbacd820-4397-4941-b2e4-fcc233a146d6.JPG)

    Berdasarkan rumus diatas, akurasi adalah metrics yang merupakan rasio dari prediksi benar (true positive dan true negative) dengan keseluruhan hasil prediksi.

* Precision

    ![prescision](https://user-images.githubusercontent.com/61934759/136345700-cc1cc1d9-9f05-4577-8165-6f368e6cf226.JPG)

    Precision merupakan rasio prediksi true positif dibandingkan dengan keseluruha hasil prediksi yang positif (true positif dan false positif)
* Recall

    ![recall](https://user-images.githubusercontent.com/61934759/136345694-2c2489bf-de0e-4928-9111-3fe18376078c.JPG)

    Merupakan rasio prediksi benar positif dibandingkan dengan keseluruhan data yang benar positif. 

* F1-score

    ![f1score](https://user-images.githubusercontent.com/61934759/136345295-45395268-e28d-4123-b5f9-85952e061b1d.JPG)

    F1 Score adalah perbandingan rata-rata presisi dan recall yang dibobotkan.Dan kelemahan pada metriks f1-score adalah tidak diperhitungkannya hasil prediksi benar pada label negatif.

Hasil evaluasi pada model baseline dan model tuning adalah sebagai berikut,
![metriks](https://user-images.githubusercontent.com/61934759/136347152-c44abe10-a652-42a3-aded-55a52727086f.JPG)

Kemudian untuk mencari fitur yang paling berpengaruh, mari kita visualisasikan _feature importances_ dari model,
![fitur](https://user-images.githubusercontent.com/61934759/136642355-651913a6-0274-40c4-86cc-5b77b0e873bf.JPG)

Dari visualisasi tersebut dapat dilihat bahwa 3 fitur paling berpengaruh pada prediksi kualitasi wine adalah tingkat alcohol, sulphates, dan total sulfur dioxide.

## Referensi
* `[1]` V. Preedy, and M. L. R. Mendez, “Wine Applications with Electronic Noses,” in Electronic Noses and Tongues in Food Science, Cambridge, MA, USA: Academic Press, 2016, pp. 137-151.
* `[2]` P. Shruthi, “Wine Quality Prediction Using Data Mining,” 1st Int. Conf. Adv. Technol. Intell. Control. Environ. Comput. Commun. Eng. ICATIECE 2019, pp. 23–26, 2019, doi: 10.1109/ICATIECE45860.2019.9063846.




