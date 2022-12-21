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


def about_view(request):
    context = {'title': 'О нас', 'cssFile': 'css/О-нас.css'}
    return render(
        request,
        'О-нас.html',
        context=context,
    )


def contacts_view(request):
    context = {'title': 'Контакты', 'cssFile': 'css/Контакты.css'}
    return render(
        request,
        'Контакты.html',
        context=context,
    )


def vm_create_view(request):
    context = {'title': 'Создание виртуальных машин', 'cssFile': 'css/Создание-виртуальных-машин.css'}
    return render(
        request,
        'Создание-виртуальных-машин.html',
        context=context,
    )


def vm_list_view(request):
    context = {'title': 'Список виртуальных машин', 'cssFile': 'css/Список-машин.css',
               'all_VM': VirtualMachine.objects.all(), 'password': ' '}
    return render(
        request,
        'Список-машин.html',
        context=context,
    )


def vm_view(request, vm_name):
    context = {'title': f'Шаблон \"{vm_name}\"', 'cssFile': 'css/Список-машин.css',
               'vm': VirtualMachine.objects.get(name=vm_name)}
    return render(
        request,
        'Шаблон-виртуальной-машины.html',
        context=context,
    )


def create_virtual_machine_view(request):
    vm_name = request.POST.get('vm_name')
    create_virtual_machine(vm_name)
    return redirect('vmList')


def delete_virtual_machine_view(request):
    vm_name = request.POST.get('vm_name')
    delete_virtual_machine(vm_name)
    return redirect('vmList')


def delete_all_virtual_machine_view(request):
    delete_all_virtual_machine()
    return redirect('vmList')
