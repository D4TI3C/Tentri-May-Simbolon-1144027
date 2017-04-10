# Ruang Keadaan

## Latar Belakang Masalah
Ruang keadaan adalah cara untuk mendefenisikam permasalahan kedalam bentuk representasi algoritma. Masalah yang dapat didefinisikan yaitu masalah yang masuk akal atau yang merupakan keadaan yang mungkin. <br>

Dalam  ruang keaadaan kita dapat memahami sebuah masalah dengan baik, maka kita harus : <br>
1.	Mendefenisikan suatu ruang keadaan tersebut
2.	Menetapkan satu atau lebih keadaan awal
3.	Menetapkan tujuan
4.	Menetapkan kumpulan aturan

Ada beberapa cara untuk mendefenisikan sebuah ruang keadaan, yaitu <br>
1.	Graf keadaan
Cara untuk menunjukan keadaan yang terdiri dari node-node  yang dihubungkan dengan menggunakan busur yang diberi anak apanah untuk menunjukan arah dan node-node ini menunjukan keadaan yang dimaksud yaitu keadaan awal dan keaadaan baru yang akan dicapai dengan menggunakan operator. <br>

2.	Pohon pelacakan
Pohon Pelacaka  merupakan cara untuk menunjukan keadaan dimana prosesnya tidak ada terjadi siklus untun mencapai tujuan yang diinginkan. Kelamahannya hanya membuthkan waktu yang lama. <br>
3.	Pohon AND/OR
Untuk mengantisipasi  kelemahan yang ada pada pohon pelacakan kita dapat menggunakan pohon AND/OR.<br>



* Contoh :<br>
Game Petani Menyebrang <br>
Kondisi awal 
Pulau kiri : ( p,a,g,h)
	          ( I,I,I,I,)
Pulau  kanan : ( p,a,g,h )
		   ( o,o,o,o )
Kondisi Akhir
Pulau kiri : ( o,o,o,o )
Pulau kanan ( I,I,I,I,)
Aturan :
1.	Petani menyebrang
2.	Petani baik
3.	Ayam menyebrang
4.	Ayam balik
5.	Gabah menyebrang
6.	Gabah balik
7.	Harimau Menyebrang
8.	Harimau balik

Solusi :
Pulau kiri
( p,a,g,h)	Pulau kanan
( p,a,g,h )	Aturan yang dijalankan
1.	(I,I,I,i)	(o,o,o,o)	
2.	(o,o,I,i)	(I,I,o,o)	1,3
3.	(I,o,I,i)	(o,I,o,o)	2
4.	(o,o,I,o)	(I,I,o,i)	1.7
5.	(I,I,I,o)	(o,o,o,i)	2.4
6.	(o,I,o,o)	(i,o,I,i)	1.5
7.	(I,I,o,o)	(o,o,I,i)	2
8.	(o,o,o,o)	(I,I,I,I,)	1.3

## Kesimpulan
Dari pernyataan diatas dapat diambil kesimpulan bahwa Mendefinisikan suatu ruang keadaan, Menetapkan satu atau lebih keadaan awal (initial state) , Menetapkan satu atau lebih tujuan (goal state),Menetapkan kumpulan aturan

## Saran
Dari kesimpulan yang dibuat sebaiknya proses yang ada pada ruang keadaan dapat diimplementasikan untuk mencapai sebuah keadaan baru dengan menggunakan operator yang tersedia. <br>

Nama : Tentri May Simbolon
NPM : 1144027
Kelas : D4 Teknik Informatika 3C
Kampus : Politeknik Pos Indonesia

Link Matkuliah : Kecerdasan Buatan


Link Plagiarisme :
Smallseotools
https://drive.google.com/open?id=0B7tQon2iaQFddG41UUJZamc3M0k 
searcheingenerrepost
https://drive.google.com/open?id=0B7tQon2iaQFdbGRvR3E5NzVYMDQ 
Referensi : Matakuliah Kecerdasan Buatan 

 
