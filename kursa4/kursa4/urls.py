from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from MySite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index'),
    path('about', views.about_view, name='about'),
    path('contacts', views.contacts_view, name='contacts'),
    path('vm-create', views.vm_create_view, name='vmCreate'),
    path('vm-list', views.vm_list_view, name='vmList'),
    path('vm/<str:vm_name>', views.vm_view, name='vm'),
    path('create_virtual_machine', views.create_virtual_machine_view, name='CreateVirtualMachine'),
    path('delete_virtual_machine', views.delete_virtual_machine_view, name='DeleteVirtualMachine'),
    path('delete_all_virtual_machine', views.delete_all_virtual_machine_view, name='DeleteAllVirtualMachine'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
