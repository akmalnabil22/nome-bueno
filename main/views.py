from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Sendok Sup Abad 17',
        'price': '17000',
        'description': 'Sendok sup yang digunakan kelas petani pada abad 17'
    }

    return render(request, "main.html", context)
