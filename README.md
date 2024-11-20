# [Nome Bueno](http://akmal-nabil-nomebueno.pbp.cs.ui.ac.id)
[Tugas 2](#tugas-2)  
[Tugas 3](#tugas-3)  
[Tugas 4](#tugas-4)  
[Tugas 5](#tugas-5)  
[Tugas 6](#tugas-6)  

# TUGAS 2
1. Langkah-langkah membuat project Django  
    - Membuat sebuah proyek Django baru  
        Untuk membuat sebuah proyek Django, kita menggunakan perintah `django-admin startproject nama_project .` di directory yang kita inginkan. Perintah tersebut, Django akan membuat direktori baru yang diberi nama sesuai `nama_project` yang berisi file-file yang dibutuhkan untuk membuat aplikasi web

    - Membuat aplikasi dengan nama `main`  
        Di dalam direktori proyek, jalankan perintah `python manage.py startapp main`. Perintah tersebut membuat direktori baru bernama `main` yang berisi file-file yang digunakan untuk mengatur fungsi dari aplikasi yang kita buat.

    - Melakukan routing pada proyek agar dapat menjalankan aplikasi `main`  
        Agar bisa melakukan routing, kita harus membuat file `urls.py` di dalam main. Dis file ini, kita mendefinisikan pola URL dari aplikasi main di proyek kita. Lalu, kita menambahkan URL main ke dalam URL proyek melalui `urls.py` yang ada di direktori proyek

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

![Screenshot (123)](https://github.com/user-attachments/assets/81cee5e7-0e5c-469a-8015-a62d876e4b2e)
![Screenshot (124)](https://github.com/user-attachments/assets/7c5d299b-9df6-4a84-a71e-37c40875a320)
![Screenshot (125)](https://github.com/user-attachments/assets/fa210eb3-429b-4017-b4e3-ab05aa54d561)
![Screenshot (126)](https://github.com/user-attachments/assets/1815700e-18ff-448e-bbad-a770c1d44f5e)



# TUGAS 4 
1. Perbedaan `HttpResponseRedirect()` dan `redirect()`  
    `HttpResponseRedirect()` dan `redirect()` memiliki fungsi yang sama, yaitu mengalihkan pengguna ke url lain. Perbedaan kedua fungsi tersebut terletak pada parameter yang diterima. `HttpResponseRedirect()` hanya menerima absolute url sebagai parameter, sedangkan `redirect()` bisa menerima url, view name, atau object sebagai parameter lalu dikonversi menjadi url yang tepat.

2. Cara menghubungkan `Product` dengan `User`  
    Untuk menghubungkan `Product` dengan `User`, baris berikut pada model yang kita buat 
    ```python 
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
    ``` 
    baris tersebut akan menghubungkan model `Product` dengan `User` yang sedang login melalui sebuah relasi. Foreign Key dari model akan merujuk ke sebuah entri `User`. Ketika sebuah objek User dihapus, maka semua model yang terikat ke User tersebut juga akan dihapus di database. 

3. Perbedaan authentication dan authorization  
    Authentication adalah proses untuk memastikan pengguna ada di database, sedangkan authorization adalah memastikan hak akses pengguna yang sudah diotentikasi. Pada django, kita menggunakan fungsi `authenticate` untuk melakukan otentikasi pengguna yang login. Untuk melakukan authorization pada django, kita menambah decorator `login_required` dan menghubungkan setiap model dengan sebuah user. 

4. Cookies :cookie:  
    Django mengingat pengguna yang login dengan menggunakan session ID dan cookies. Setiap pengguna yang login akan dibuatkan session ID yang disimpan di server dan cookies yang disimpan di client. Cookies juga digunakan untuk menyimpan preferensi pengguna, melacak aktivitas pengguna di situs web, dan otentikasi. Tidak semua cookies aman digunakan karena keamanan cookies bergantung pada bagaimana cookies dikelola. Jika cookies tidak diamankan dengan baik, maka akan rentan dengan ancamanan keamanan. 

5. Implementasi checklist  
    - Implementasi fungsi registrasi, login, dan logout  
    fungsi registrasi 
    ``` python 
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)
    ``` 
    fungsi login 
    ``` python 
    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                user = form.get_user()
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response

        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)
    ``` 
    fungsi logout 
    ```python 
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ``` 

    - Membuat dua akun dengan tiga data  
    Untuk membuat dua akun, maka perlu dilakukan registrasi dua akun berbeda. Lalu pada masing-masing akun, tambahkan tiga produk. 

    - Menghubungkan model `Product` dengan `User`  
    hubungkan `Product` ke `User` dengan menggunakan `ForeignKey` 
    ```python 
    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
    ``` 

    - Menampilkan detail informasi pengguna yang sedang login  
    Untuk menampilkan username pengguna yang sedang login, maka fungsi `show_main` perlu diubah 
    ```python 
    def show_main(request):
        product_entries = Product.objects.filter(user=request.user)

        context = {
            'appname': 'Nome Bueno',
            'name': request.user.username,
            'class': 'E',
            'product_entries': product_entries,
            'last_login': request.COOKIES['last_login'],
        }

        return render(request, "main.html", context)
    ``` 
    Lalu, pada fungsi login, kita membuat cookie last_login dan menambahkannya ke response untuk menampilkan last login pada halaman utama 
    ```python 
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response 
    ``` 
    Tampilkan `last_login` di halaman main 
    ``` 
    <h5>Sesi terakhir login: {{ last_login }}</h5> 
    ```  

# Tugas 5  
1. Urutan pengambilan CSS Selector
    1. ID selector, memilih elemen berdasarkan ID  
    2. Class selector, memilih elemen berdasarkan class  
    3. Element selector, memilih elemen berdasarkan tag  

2. Pentingnya Responsive design  
    Responsive design memastikan aplikasi web bisa menyesuaikan dengan ukuran layar pengguna. Tanpa adanya responsive design, pengguna bisa kesulitan membaca dan berinteraksi dengan aplikasi. Dengan adanya responsive design, *user experience* bisa meningkat.  
    Contoh aplikasi yang sudah menerapkan responsive design: SCELE, Github  
    Contoh aplikasi yang belum menerapkan responsive design: SIAK-NG  

3. Perbedaan `margin`, `border`, `padding`  
    - `margin` adalah ruang kosong di luar elemen  
    ```html
    <div style="margin: 20px;">Ini adalah elemen dengan margin 20px di semua sisi.</div> 
    ```
    - `border` adalah garis yang mengelilingi elemen  
    ```html
    <div style="border: 2px solid black;">Ini adalah elemen dengan border hitam 2px.</div>
    ```
    - `padding` adalah ruang kosong di dalam elemen (di antara border dan konten elemen)  
    ```html
    <div style="padding: 10px;">Ini adalah elemen dengan padding 10px di dalamnya.</div>
    ```

4. *Flex box* dan *grid layout*  
    - *Flex box* adalah tata letak satu dimensi, baik horizontal maupun vertikal, yang memudahkan pembuatan tata letak responsif dan fleksibel. *Flexbox* cocok untuk tata letak satu dimensi seperti bar navigasi, menu, dan daftar item  
    - *Grid layout* adalah tata letak dua dimensi yang terdiri dari baris dan kolom. *Grid* cocok digunakan untuk layout kolom dan baris yang rumit seperti kartu produk e-commerce  

5. Implementasi Checklist  
    - fungsi edit dan hapus product  
    ```python
    def edit_product(request, id):
        product = Product.objects.get(pk = id)

        form = ProductEntryForm(request.POST or None, instance=product)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "edit_product.html", context)
    
    def delete_product(request, id):
    
        product = Product.objects.get(pk = id)
        
        product.delete()
        
        return HttpResponseRedirect(reverse('main:show_main'))
    ```  
    - kustomisasi halaman login, register, dan tambah product  
    [Halaman login](./main/templates/login.html)  
    [Halaman register](./main/templates/register.html)  
    [Halaman tambah product](./main/templates/create_product_entry.html)  
    - Kustomisasi halaman daftar product  
        Jika product kosong  
        ```html
        {% if not product_entries %}
        <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'image/pinched-fingers.png' %}" alt="Pinched Finges Emoji" class="w-32 h-32 mb-4"/>
            <p class="text-center text-gray-600 mt-4">Belum ada data product pada Nome Bueno.</p>
        </div>
        ```  
        Jika product ada  
        ```html
        {% else %}
        <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
            {% for product_entry in product_entries %}
                {% include 'card_product.html' with product_entry=product_entry %}
            {% endfor %}
        </div>
        {% endif %}
        ```
        [Card product](./main/templates/card_product.html)  
    - Button edit dan delete pada card product  
     ```h
    <div class="absolute top-0 -right-4 flex space-x-1">
        <a href="{% url 'main:edit_product' product_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
            </svg>
        </a>
        <a href="{% url 'main:delete_product' product_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
            </svg>
        </a>
    </div>
    ```
    - [Implementasi navbar](./templates/navbar.html)  

# Tugas 6  
1. Manfaat JavaScipt  
    - JavaScript memungkinkan elemen interaktif bisa ditambahkan ke dalam web.  
    - JavaScript juga bisa melakukan pengambilan data dari server tanpa memuat ulang halaman dengan menggunakan AJAX (Asynchronous JavaScript and XML)  
    -  JavaScript memungkinkan pengembang untuk mengakses dan memodifikasi elemen HTML dan struktur DOM (Document Object Model) secara dinamis.  
    - JavaScript bisa dijalankan di hampir semua browser modern.  
    - Memiliki banyak framework dan library yang bisa dipakai seperti jQuery, React, Angular, dan Vue.js.  

2. fungsi penggunaan `await`  
    `await` akan memberhentikan eksekusi kode di dalam blok asinkron sampai `promise` yang dihasilkan oleh `fetch()` diselesaikan. Dengan kata lain, `await` memastikan bahwa data dari server diambil sebelum melanjutkan ke instruksi berikutnya. `fetch()` sendiri mengembalikan sebuah `promise`. Tanpa `await`, hasil dari `promise` akan tetap menjadi objek `promise` dan tidak langsung berisi data dari server. Ini dapat menyebabkan masalah jika kita mencoba mengakses data yang belum diterima.  

3. `csrf_exempt`  
    Kita perlu menggunakan `csrf_exempt` pada view yang akan digunakan untuk AJAX POST karena Django secara otomatis mengaktifkan CSRF protection untuk semua POST request. Saat melakukan AJAX POST request dari JavaScript, jika CSRF token tidak disertakan dengan benar dalam request, Django akan menolak request tersebut dengan mengirimkan error 403 Forbidden. Untuk bypass sementara pada request AJAX yang tidak memiliki CSRF token, kita dapat menandai view dengan decorator `@csrf_exempt`, yang menonaktifkan pengecekan CSRF untuk view tersebut.  

4. Pembersihan data input di *backend*  
    Melakukan pembersihan data di backend memastikan bahwa semua data yang masuk ke sistem tetap valid dan aman, bahkan jika seseorang mencoba memanipulasi data input dari frontend. Pembersihan di frontend dapat dimanipulasi atau dilewati oleh pengguna yang berpengalaman. Mereka bisa mematikan atau mengubah kode JavaScript di browser mereka, lalu mengirimkan data mentah langsung ke server. Pembersihan di backend memastikan bahwa manipulasi tersebut tidak merusak aplikasi, menghindari serangan XSS (Cross-Site Scripting), SQL Injection, atau serangan lainnya.  

5. Implementasi checklist  
    - mengubah `cards` agar mendukung  AJAX `GET`  
        Hapus bagian conditional if pada `main.html` dan tambahkan line berikut  
        ```html
        <div id="product_entry_cards"></div>
        ```
        Buat sebuah fungsi JavaScript  
        ```js
        async function refreshProductEntries() {
            document.getElementById("product_entry_cards").innerHTML = "";
            document.getElementById("product_entry_cards").className = "";
            const productEntries = await getproductEntries();
            let htmlString = "";
            let classNameString = "";

            if (productEntries.length === 0){
            classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
            htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
                <img src="{% static 'image/pinched-fingers.png' %}" alt="Pinched Finges Emoji" class="w-32 h-32 mb-4"/>
                <p class="text-center text-gray-600 mt-4">Belum ada data product pada Nome Bueno.</p>
            </div>
            `;
            }
            else{
            classNameString = "columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full"
            productEntries.forEach((item) => {
                const name = DOMPurify.sanitize(item.fields.name);
                const description = DOMPurify.sanitize(item.fields.description);
                htmlString +=`
                <div class="relative break-inside-avoid">
                <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
                    <div class="flex flex-col w-[3rem] h-8 bg-transparent rounded-md">
                    <img src="{% static 'image/pin.png' %}" alt="pin" />
                    </div>
                </div>
                <div class="relative top-5 bg-orange-100 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-orange-300 transform rotate-1 hover:rotate-0 transition-transform duration-300">
                    <div class="bg-orange-400 text-gray-800 p-4 rounded-t-lg border-b-2 border-orange-500">
                    <h3 class="font-bold text-xl mb-2 text-center pt-1">${name}</h3>
                    <p class="text-gray-600 text-center font-semibold">Rp.${item.fields.price}</p>
                    </div>
                    <div class="p-4">
                    <p class="font-semibold text-lg mb-2 text-center">Description</p> 
                    <p class="text-gray-700 mb-2">
                        <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#CDC1FF_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">${description}</span>
                    </p>
                    </div>
                </div>
                <div class="absolute top-0 -right-4 flex space-x-1">
                    <a href="/edit-product/${item.pk}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                        <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                    </svg>
                    </a>
                    <a href="/delete/${item.pk}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
                        <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                    </a>
                </div>
                </div>
                `;
            });
            }
            document.getElementById("product_entry_cards").className = classNameString;
            document.getElementById("product_entry_cards").innerHTML = htmlString;
        }
        ```  
    - mengambil data product pengguna yang login dengan AJAX `GET`   
        modifikasi fungsi `show_json` agar mengambil data pemgguna login  
        ```python
        def show_json(request):
            data = Product.objects.filter(user=request.user)
            return HttpResponse(serializers.serialize('json', data), content_type='application/json')
        ```   
        buat fungsi JavaSript   
        ```js
        async function getproductEntries(){
            return fetch("{% url 'main:show_json' %}").then((res) => res.json())
        }
        ```   
    - Tombol untuk membuka modal dengan form untuk menambah produk  
        buat sebuah fungsi yang akan menunjukkan modal  
        ```js
        function showModal() {
            const modal = document.getElementById('crudModal');
            const modalContent = document.getElementById('crudModalContent');

            modal.classList.remove('hidden'); 
            setTimeout(() => {
                modalContent.classList.remove('opacity-0', 'scale-95');
                modalContent.classList.add('opacity-100', 'scale-100');
            }, 50); 
        }
        ```  
        Buat tommbol yang akan membuka modal pada halaman utama  
        ```html
        <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="btn bg-lime-700 hover:bg-lime-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105" onclick="showModal();">
          Add New Product by AJAX
        </button>
        ```  
    - Fungsi *view* yang menambahkan product  
        ```python
        @csrf_exempt
        @require_POST
        def add_product_entry_ajax(request):
            name = strip_tags(request.POST.get("name"))
            price = request.POST.get("price")
            description = strip_tags(request.POST.get("description"))
            user = request.user

            new_product = Product(
                name=name, description=description,
                price=price,
                user=user
            )
            new_product.save()

            return HttpResponse(b"CREATED", status=201)
        ```  
    - Buat path yang mengarah pada fungsi yang baru dibuat  
        ```python
        path('create-product-entry-ajax/', add_product_entry_ajax, name="add_product_entry_ajax"),
        ```
    - Menghubungkan form modal dengan path yang baru dibuat  
        ```js
        function addProductEntry() {
            fetch("{% url 'main:add_product_entry_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#productEntryForm')),
            })
            .then(response => {
                if (response.ok) {
                refreshProductEntries();
                hideModal();  
                document.getElementById("productEntryForm").reset();  
                } else {
                console.error('Error adding product entry:', response.statusText);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });

            return false;
            }
        ```
    - Refresh pada halaman utama secara asinkronus untuk menampilkan data baru  
        panggil fungsi refresh yang telah dibuat  
        ```js
        refreshProductEntries();
        ```

            