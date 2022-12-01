from django.shortcuts import render, redirect

from Programm.CreatingVM import *
from .models import *


def index(request):
    context = {'title': 'Главная', 'cssFile': 'css/Главная.css'}
    return render(
        request,
        'Главная.html',
        context=context,
    )


def about(reqest):
    context = {'title': 'О нас', 'cssFile': 'css/О-нас.css'}
    return render(
        reqest,
        'О-нас.html',
        context=context,
    )


def contacts(reqest):
    context = {'title': 'Контакты', 'cssFile': 'css/Контакты.css'}
    return render(
        reqest,
        'Контакты.html',
        context=context,
    )


def vmCreate(reqest):
    context = {'title': 'Создание виртуальных машин', 'cssFile': 'css/Создание-виртуальных-машин.css'}
    return render(
        reqest,
        'Создание-виртуальных-машин.html',
        context=context,
    )


def vmList(reqest):
    context = {'title': 'Список виртуальных машин', 'cssFile': 'css/Список-машин.css',
               'all_VM': VirtualMachine.objects.all()}
    return render(
        reqest,
        'Список-машин.html',
        context=context,
    )


def CreatedVirtualMachine(reqest, vm_name):
    CreateVirtualMachine(vm_name)
    return redirect('vmList')


def DeletedVirtualMachine(reqest, vm_name):
    DeleteVirtualMachine(vm_name)
    return redirect('vmList')
