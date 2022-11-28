from django.contrib import admin

from MySite.models import VirtualMachine


class VirtualMachineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'running')
    list_display_links = ('name',)
    search_fields = ('name',)


admin.site.register(VirtualMachine, VirtualMachineAdmin)
