# Generated by Django 4.1.3 on 2022-11-28 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualMachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('zone', models.CharField(choices=[('ru-central1-a', 'ru-central-a'), ('ru-central1-b', 'ru-central-b'), ('ru-central1-c', 'ru-central-c')], default='ru-central1-a', max_length=13, verbose_name='Зона доступности')),
                ('image_id', models.CharField(choices=[('fd8bh0c781u19q50m4kj', 'Ubuntu-22.04'), ('fd8e65d4chiel4ussa9o', 'Debian-11'), ('fd84go2nk3voj0gg7tpn', 'openSUSE-Leap-15.3'), ('fd8bv62nmsjf6hmjrh96', 'AlmaLinux-8'), ('fd8nce10ece89ufqkk9t', 'Astra-Linux-Common-Edition-2.12'), ('fd8i8fljrbbcclckhlm9', 'ALT-Linux-10'), ('fd8jvcoeij6u9se84dt5', 'CentOS-7'), ('fd8phu675e6sgsa68pvj', 'Fedora-35'), ('fd865udut6b1gvgh5igh', 'Fedora-CoreOS-35'), ('fd8mnkj7vk131q9ll4p5', 'CentOS-Stream-8'), ('fd8q0kjl4l1iovds9f29', 'REDOS-7.3')], default='fd8phu675e6sgsa68pvj', max_length=20, verbose_name='Операционная система')),
                ('boot_disk_type', models.CharField(choices=[('network-hdd', 'HDD'), ('network-ssd', 'SSD'), ('network-ssd-nonreplicated', 'NR-SSD')], default='network-hdd', max_length=25, verbose_name='Тип диска')),
                ('boot_disk_size', models.IntegerField(default=15, verbose_name='Размер диска')),
                ('cores', models.IntegerField(default=2, verbose_name='vCPU')),
                ('core_fraction', models.IntegerField(choices=[(20, '20%'), (50, '50%'), (100, '100%')], default=20, verbose_name='Гарантированная доля vCPU')),
                ('memory', models.IntegerField(default=2, verbose_name='RAM')),
                ('username', models.CharField(max_length=20, verbose_name='Имя пользователя')),
                ('ssh_key', models.CharField(max_length=500, verbose_name='SSH-ключ')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
