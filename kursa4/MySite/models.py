from django.db import models
from django.urls import reverse


class VirtualMachine(models.Model):
    name = models.CharField(max_length=40, unique=True, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    ZONE = [
        ('ru-central1-a', 'ru-central-a'),
        ('ru-central1-b', 'ru-central-b'),
        ('ru-central1-c', 'ru-central-c'),
    ]
    zone = models.CharField(choices=ZONE, max_length=13, default='ru-central1-a', verbose_name='Зона доступности')

    IMAGE_ID = [
        ('fd8bh0c781u19q50m4kj', 'Ubuntu-22.04'),
        ('fd8e65d4chiel4ussa9o', 'Debian-11'),
        ('fd84go2nk3voj0gg7tpn', 'openSUSE-Leap-15.3'),
        ('fd8bv62nmsjf6hmjrh96', 'AlmaLinux-8'),
        ('fd8nce10ece89ufqkk9t', 'Astra-Linux-Common-Edition-2.12'),
        ('fd8i8fljrbbcclckhlm9', 'ALT-Linux-10'),
        ('fd8jvcoeij6u9se84dt5', 'CentOS-7'),
        ('fd8phu675e6sgsa68pvj', 'Fedora-35'),
        ('fd865udut6b1gvgh5igh', 'Fedora-CoreOS-35'),
        ('fd8mnkj7vk131q9ll4p5', 'CentOS-Stream-8'),
        ('fd8q0kjl4l1iovds9f29', 'REDOS-7.3'),
    ]
    image_id = models.CharField(choices=IMAGE_ID, max_length=20, default='fd8phu675e6sgsa68pvj',
                                verbose_name='Операционная система')

    BOOT_DISK_TYPE = [
        ('network-hdd', 'HDD'),
        ('network-ssd', 'SSD'),
        ('network-ssd-nonreplicated', 'NR-SSD'),
    ]
    boot_disk_type = models.CharField(max_length=25, choices=BOOT_DISK_TYPE, default='network-hdd',
                                      verbose_name='Тип диска')
    boot_disk_size = models.IntegerField(verbose_name='Размер диска', default=15)

    cores = models.IntegerField(verbose_name='vCPU', default=2)
    CORE_FRACTION = [
        (20, '20%'),
        (50, '50%'),
        (100, '100%'),
    ]
    core_fraction = models.IntegerField(choices=CORE_FRACTION, verbose_name='Гарантированная доля vCPU', default=20)
    memory = models.IntegerField(verbose_name='RAM', default=2)

    username = models.CharField(max_length=20, verbose_name='Имя пользователя', default='user')
    ssh_key = models.CharField(max_length=500, verbose_name='SSH-ключ')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    running = models.BooleanField(verbose_name='Активна', default=True)

    class Meta:
        verbose_name = 'Виртуальные машины'
        verbose_name_plural = 'Виртуальные машины'
        ordering = ['time_create']

    def get_absolute_url(self):
        return reverse('vm', kwargs={'vm_id': self.pk})

    def __str__(self):
        return self.name
