### tuple
Tuple sudah banyak kali dijelaskan dari sudut interface atau spesifikasinya, tapi jarang sekali dibahas dari sisi implementasi struktur datanya. Materi mengenai struktur data dapat kita rujuk dari materi kuliah terbuka "MIT OCW 6.006 Introduction to Algorithms".
Tuple tidak mendukung operasi append, atau insert sehingga mengesankan bahwa ia adalah objek container dengan struktur fixed array berisi pointers yang masing masing menunjuk ke objek anggota tuple. Dengan elemen pointers yang seragam, sama ukurannya, misalnya dalam sistem 64 bit digunakan 8 bytes, maka pada struktur fixed array kita dapat mengakses elemen anggota secara langsung tidak tergantung dari banyaknya anggota, seperti mengakses random access memory, alamat elemen pada indeks k, adalah alamat indeks awal ditambah size pointer dikalikan indeks k, atau pada notasi big-O adalah O(1). Tetapi fixed array memiliki kelemahan pada operasi insert yang memerlukan pergeseran elemen, dan tuple tidak mendukung operasi mutable ini.
Lain lagi dengan struktur link list, akses anggota elemen menjadi lebih lambat, linear O(n), karena harus ditelusuri linknya satu per satu, walaupun untuk operasi append/insert ringan, O(1), karena hanya menyangkut perubahan link antar elemen.
Karakteristik Tuple lebih condong ke arah fixed array, artinya untuk operasi pada data permanen kita akan mendapat *akses yang cepat, ringan, hemat memori* bila menggunakan tuple.