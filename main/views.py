from django.shortcuts import render

def show_main(request):
    context = {
        'appname': 'Nome Bueno',
        'name': 'Akmal Nabil Fikri',
        'class': 'E'
    }

    return render(request, "main.html", context)
