from django.contrib import admin

from MySite.models import VirtualMachine


class VirtualMachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'time_update', 'running')
    list_display_links = ('name',)
    search_fields = ('name',)
    # list_editable = ('running',)
    list_filter = ('running', 'time_create')
    fields = (
    'name', 'description', 'zone', 'image_id', 'boot_disk_type', 'boot_disk_size', 'cores', 'core_fraction', 'memory',
    'username', 'ssh_key', 'running', 'time_create', 'time_update')
    readonly_fields = ('time_create', 'time_update', 'running')


admin.site.register(VirtualMachine, VirtualMachineAdmin)

admin.site.site_title = 'Сайт для создания виртуальных машин'
admin.site.site_header = 'Администрирование сайта'
admin.site.index_title = 'Администриование'
