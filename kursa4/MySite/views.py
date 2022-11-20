from django.shortcuts import render

def index(request):
    return render(
        request,
        'Главная.html',
    )

def about(reqest):
    return render(
        reqest,
        'О-нас.html'
    )

def contacts(reqest):
    return render(
        reqest,
        'Контакты.html',
    )

def vmCreate(reqest):
    return render(
        reqest,
        'Создание-виртуальных-машин.html',
    )

def vmList(reqest):
    return render(
        reqest,
        'Список-машин.html',
    )

