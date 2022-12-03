from django.shortcuts import render, redirect

from Programm.CreatingVM import *
from .models import *


def index_view(request):
    context = {'title': 'Главная', 'cssFile': 'css/Главная.css'}
    return render(
        request,
        'Главная.html',
        context=context,
    )


def about_view(reqest):
    context = {'title': 'О нас', 'cssFile': 'css/О-нас.css'}
    return render(
        reqest,
        'О-нас.html',
        context=context,
    )


def contacts_view(reqest):
    context = {'title': 'Контакты', 'cssFile': 'css/Контакты.css'}
    return render(
        reqest,
        'Контакты.html',
        context=context,
    )


def vm_create_view(reqest):
    context = {'title': 'Создание виртуальных машин', 'cssFile': 'css/Создание-виртуальных-машин.css'}
    return render(
        reqest,
        'Создание-виртуальных-машин.html',
        context=context,
    )


def vm_list_view(reqest):
    context = {'title': 'Список виртуальных машин', 'cssFile': 'css/Список-машин.css',
               'all_VM': VirtualMachine.objects.all()}
    return render(
        reqest,
        'Список-машин.html',
        context=context,
    )


def create_virtual_machine_view(reqest):
    vm_name = reqest.POST.get('vm_name')
    create_virtual_machine(vm_name)
    return redirect('vmList')


def delete_virtual_machine_view(reqest):
    vm_name = reqest.POST.get('vm_name')
    delete_virtual_machine(vm_name)
    return redirect('vmList')


def delete_all_virtual_machine_view(reqest):
    vm_name = reqest.POST.get('vm_name')
    delete_all_virtual_machine(vm_name)
    return redirect('vmList')
