# [Nome Bueno](http://akmal-nabil-nomebueno.pbp.cs.ui.ac.id)
[Tugas 2](#tugas-2)  
[Tugas 3](#tugas-3)  
[Tugas 4](#tugas-4)

# TUGAS 2
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

# TUGAS 3  
1. Pentingnya Data Delivery  
    Data delivery memungkinkan aplikasi web yang kita buat menampilkan konten dinamis. Aplikasi web dapat memuat data yang sesuai dengan interaksi pengguna. Pengguna akan mendapat informasi yang mereka butuhkan secara real-time saat mereka berinteraksi dengan aplikasi. Data delivery juga memungkinkan aplikasi pihak ketiga untuk mengambil dan mengirim data secara efisien  melalui JSON atau XML. Selain itu, Django juga memiliki fitur keamanan yang kuat seperti CSRF protection, XSS protection, dan pengelolaan sesi untuk memastikan keamanan data yang dikirim dan diterima.  

2. XML dan JSON  
    Secara umum, JSON lebih banyak dipakai dibanding XML karena JSON memiliki beberapa keunggulan sebagai berikut:  
    - JSON memiliki struktur yang lebih sederhana dan mudah dibaca dibanding XML. JSON menggunakan kurung kurawal sedangkan XML menggunakan tag pembuka dan penutup. Hal ini juga menyebabkan JSON lebih efisien untuk diproses oleh server.   
    - JSON lebih mudah diolah di JavaScript dibanding XML karena format JSON sangat mirip dengan JavaScript.  
    - Kebanyakan framework modern banyak library yang bisa bekerja dengan JSON. Di sisi lain, dukungan XML dalam pengembangan web tidak sepopuler dulu, tetapi masih digunakan di beberapa aplikasi khusus.  

3. Method `is_valid()`
    Method `is_valid()` adalah method yang digunakan untuk memeriksa apakah data yang dikirimkan melalui form sudah sesuai dengan validasi yang ada pada form tersebut. Method tersebut sangat penting digunakan untuk mencegah adanya data yang tidak sesuai aturan validasi. Data yang tidak sesuai validasi bisa berbahaya jika dimasukkan ke dalam database karena bisa menimbulkan ancaman serangan seperti SQL Injection.  

 4. `csrf_token`  
    `csrf_token` adalah nilai unik dan rahasia yang dbuat oleh server dan dibagikan ke client. Saat submit form, client harus menyertakan token CSRF pada request. Tanpa adanya `csrf_token`, web akan rentan terkena serangan CSRF. Serangan CSRF adalah sebuah serangan dimana user akan mengirimkan request mencurigakan ke web tanpa diketahui. Kemudian, user akan melakukan aksi secara tidak sengaja seperti mengubah email, mengubah password, atau melakukan transfer uang.  

5. Implementasi checklist  
    - Membuat input form  
        Untuk membuat form, pertama kita harus membuat file `forms.py` di direktori main yang berisi struktur form yang menerima data Product.  
        ```  
        from django.forms import ModelForm
        from main.models import Product

        class ProductEntryForm(ModelForm):
            class Meta:
                model = Product
                fields = ["name", "price", "description"]
        ```  
        Lalu, pada `views.py`, kita membuat fungsi baru `create_product_entry` untuk menampilkan form yang bisa menambahkan data Product.   
        ```  
        def create_product_entry(request):
            form = ProductEntryForm(request.POST or None)

            if form.is_valid() and request.method == 'POST':
                form.save()
                return redirect('main:show_main')
            
            context = {'form': form}
            return render(request, 'create_product_entry.html', context)
        ```  
        Pada fungsi `show_main`, kita menambahkan data `product_entries` yang berisi semua objek Produk.
        ``` 
        def show_main(request):
            product_entries = Product.objects.all()

            context = {
                'appname': 'Nome Bueno',
                'name': 'Akmal Nabil Fikri',
                'class': 'E',
                'product_entries': product_entries,
            }

            return render(request, "main.html", context)
        ```  
        Fungsi `create_product_entry` di*route* ke `urls.py` main.  
        ``` 
        path('create-product-entry', create_product_entry, name='create_product_entry'),
        ``` 
        Pada direktori templates main, kita membuat file html baru yang berisi form untuk menambahkan produk.  

    
    - Membuat 4 fungsi baru yang menampilkan objek dalam format XML, JSON, XML by ID, JSON, by ID.
        Untuk menambahkan 4 fungsi di atas, kita perlu import `HttpResponse` dan `Serializer` pada `views.py`. Lalu, kita menambahkan fungsi `show_xml`, `show_json`, `show_xml_by_id`, `show_json_by_id`. Bentuk keempat fungsi tersebut kurang lebih sama. Untuk `show_xml` dan `show_json`, data yang diambil adalah seluruh objek yang ada dari Produk. Sedangkan pada `show_xml_by_id` dan `show_json_by_id`, fungsi akan menerima parameter id dan data yang ditampilkan adalah objek Produk yang memiliki ID tersebut.  
        ``` 
        def show_xml(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
        ``` 
        ``` 
        def show_json(request):
            data = Product.objects.all()
            return HttpResponse(serializers.serialize('json', data), content_type='application/json')
        ``` 
        ``` 
        def show_xml_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize('xml', data), content_type='application/xml')
        ``` 
        ``` 
        def show_json_by_id(request, id):
            data = Product.objects.filter(pk=id)
            return HttpResponse(serializers.serialize('json', data), content_type='application/json')
        ``` 

    - Routing masing-masing view 
        Untuk melakukan routing, kita menambahkan url masing-masing view pada `urlpatterns` di `urls.py` pada main. 
        ``` 
        path('xml/', show_xml, name='show_xml'),
        path('json/', show_json, name='show_json'),
        path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
        ``` 

# TUGAS 4 
1. Perbedaan `HttpResponseRedirect()` dan `redirect()` 
    `HttpResponseRedirect()` dan `redirect()` memiliki fungsi yang sama, yaitu mengalihkan pengguna ke url lain. Perbedaan kedua fungsi tersebut terletak pada parameter yang diterima. `HttpResponseRedirect()` hanya menerima absolute url sebagai parameter, sedangkan `redirect()` bisa menerima url, view name, atau object sebagai parameter lalu dikonversi menjadi url yang tepat.

2. Cara kerja penghubungan `Product` dengan `User`
    