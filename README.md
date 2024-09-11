# [Nome Bueno](http://akmal-nabil-nomebueno.pbp.cs.ui.ac.id)

1. Langkah-langkah membuat project Django
    - Membuat sebuah proyek Django baru
        Untuk membuat sebuah proyek Django, kita menggunakan perintah `django-admin startproject nama_project .` di directory yang kita inginkan. Perintah tersebut, Django akan membuat direktori baru yang diberi nama sesuai `nama_project` yang berisi file-file yang dibutuhkan untuk membuat aplikasi web

    - Membuat aplikasi dengan nama `main`
        Di dalam direktori proyek, jalankan perintah `python manage.py startapp main`. Perintah tersebut membuat direktori baru bernama `main` yang berisi file-file yang digunakan untuk mengatur fungsi dari aplikasi yang kita buat.

    - Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`
        Agar bisa melakukan routing, kita harus membuat file `urls.py` di dalam main. Di file ini, kita mendefinisikan pola URL dari aplikasi main di proyek kita. Lalu, kita menambahkan URL main ke dalam URL proyek melalui `urls.py` yang ada di direktori proyek

    - Membuat model pada aplikasi `main` dengan nama `Product` dan memiliki atribut `name`, `price`, `description`
        Pada direktori main, terdapat file modes.py. Di file tersebut, kita bisa menambahkan class `Product` dengan atribut `name`, `price`, `description`. Kita juga memasukkan `model.Models` sebagai parameter `Product` untuk mendefinisikan class tersebut sebagai model Django

    - Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas
        Pada file `views.py`, buat sebuah fungsi dengan nama `show_main` yang menerima parameter `request`. Di fungsi tersebut, buat sebuah dictionary dengan nama `context` yang berisi nama aplikasi, nama, dan kelas. Lalu, fungsi tersebut akan mengembalikan fungsi render untuk menampilkan tampilan `main.html`
    
    - Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
        Pada file `urls.py` yang ada di direktori main, kita menambahkan path baru yang memanggil fungsi `show_main` yang ada di `view.py`
    
    - Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
        Di PWS, kita harus membuat proyek baru. Lalu, tambahkan proyek tersebut sebagai repositori remote dan lakukan `add`, `commit`, `push` ke repositori tersebut
    
    - Membuat sebuah README.md yang berisi tautan menuju aplikasi PWS yang sudah di-deploy
        Kita bisa menggunakan Visual Studio Code sebagai editor untuk menulis README.md. Jangan lupa lakukan push ke repositori remote.

2. [Bagan](https://drive.google.com/file/d/1xhhLIQDPAv5gxB69ZJy4rHCyw5dDe4mD/view?usp=drive_link)
    Penjelasan: `urls.py` menerima request dari browser. Kemudian `urls.py` menentukan view yang akan dipanggil sesuai dengan request dari user. Kemudian, view.py akan memanggil models.py untuk mengakses dan memroses data-data yang ada di database. Setelah itu, view.py memanggil file html untuk merender tampilan yang akan ditampilkan kepada user

3. Fungsi git dalam pengembangan perangkat lunak
    Git menyimpan catatan setiap perubahan yang dilakukan pada kode dari waktu ke waktu. Hal ini memungkinkan pengembang untuk melacak perubahan, mengidentifikasi siapa yang membuatnya, kapan dibuat, dan apa saja yang diubah. Git juga memungkinkan beberapa pengembang untuk berkolaborasi dalam sebuah proyek sekaligus. Setiap pengembang dapat melakukan modidikasi pada branch mereka sendiri tanpa mengubah kode utama.

4. Mengapa Django dijadikan permulaan pembelajaran pengembangan perangkat lunak
    Karena Django memiliki banyak sekali fitur bawaan yang berguna sehingga memudahkan pengembang perangkat lunak pemula untuk belajar membuat sebuah aplikasi web. Django juga menggunakan bahasa pemrograman python yang menyediakan berbagai macam library dan memiliki sintaks yang mudah dipahami

5. Django sebagai ORM
    Model pada Django disebut sebagai ORM karena pada model django terdapat keterikatan antara **Relational Database** dan **Object-Oriented Programming**. ORM memungkinkan pengembang untuk berinteraksi dengan database menggunakan kelas dan metode Python. Bagi para pengembang, hal ini menghasilkan interaksi database yang lebih bersih, lebih mudah dikelola, dan lebih mudah dimengerti. 