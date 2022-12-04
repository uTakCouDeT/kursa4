from MySite.models import VirtualMachine
import os


def create_vm_template(vm_name):
    vm = VirtualMachine.objects.get(name=vm_name)
    with open(f"Programm/terraform/{vm.name}.tf", "w") as tf_file:
        tf_file.write(
            f"resource \"yandex_vpc_subnet\" \"subnet_{vm.name}\" "
            "{\n"
            f"  name           = \"subnet_{vm.name}\"\n"
            f"  zone           = \"{vm.zone}\"\n"
            "  network_id     = yandex_vpc_network.network.id\n"
            "  v4_cidr_blocks = [\"192.168.10.0/24\"]\n"
            "}\n"
            "\n"
            f"resource \"yandex_compute_instance\" \"{vm.name}\" "
            "{\n"
            f"  name        = \"{vm.name}\"\n"
            f"  description = \"{vm.description}\"\n"
            "  resources {\n"
            f"    core_fraction = {vm.core_fraction}\n"
            f"    cores         = {vm.cores}\n"
            f"    memory        = {vm.memory}\n"
            "  }\n"
            "  boot_disk {\n"
            "    initialize_params {\n"
            f"      image_id = \"{vm.image_id}\"\n"
            f"      type     = \"{vm.boot_disk_type}\"\n"
            f"      size     = {vm.boot_disk_size}\n"
            "    }\n"
            "  }\n"
            "  network_interface {\n"
            "    subnet_id = yandex_vpc_subnet.subnet.id\n"
            "    nat       = true\n"
            "  }\n"
            "  metadata = {\n"
            f"    user-data = file(\"meta_{vm.name}.txt\")\n"
            "  }\n"
            "  service_account_id = \"ajecupuvdpp99gv58j84\"\n"
            "}\n"
            "\n"
            f"output \"internal_ip_address_{vm.name}\" "
            "{\n"
            f"  value = yandex_compute_instance.{vm.name}.network_interface.0.ip_address\n"
            "}\n"
            "\n"
            f"output \"external_ip_address_{vm.name}\" "
            "{\n"
            f"  value = yandex_compute_instance.{vm.name}.network_interface.0.nat_ip_address\n"
            "}\n"
        )
    with open(f"Programm/terraform/meta_{vm.name}.txt", "w") as tf_file:
        tf_file.write(
            f"""#cloud-config
users:
  - name: {vm.username}
    groups: sudo
    shell: /bin/bash
    sudo: ['ALL=(ALL) NOPASSWD:ALL']
    ssh_authorized_keys:
      - ssh-rsa {vm.ssh_key}
"""
        )


def delete_vm_template(vm_name):
    if os.path.exists(f"Programm/terraform/{vm_name}.tf"):
        os.remove(f"Programm/terraform/{vm_name}.tf")
    if os.path.exists(f"Programm/terraform/meta_{vm_name}.txt"):
        os.remove(f"Programm/terraform/meta_{vm_name}.txt")


def run_terraform_apply_and_change_running_flag(vm):
    # os.startfile(r"Programm\terraform\terraform_apply.ps1")
    vm.running ^= True
    vm.save()


def create_virtual_machine(vm_name):
    create_vm_template(vm_name)

    vm = VirtualMachine.objects.get(name=vm_name)
    run_terraform_apply_and_change_running_flag(vm)

    with open("Programm/logs.txt", "a") as log_file:
        log_file.write(f"[{vm.time_update}] created vm: {vm.name}\n")


def delete_virtual_machine(vm_name):
    delete_vm_template(vm_name)

    vm = VirtualMachine.objects.get(name=vm_name)
    run_terraform_apply_and_change_running_flag(vm)

    with open("Programm/logs.txt", "a") as log_file:
        log_file.write(f"[{vm.time_update}] deleted vm: {vm.name}\n")


def delete_all_virtual_machine(vm_name):
    vm_all = VirtualMachine.objects.all()
    for vm in vm_all:
        if vm.running:
            delete_vm_template(vm_name)
    # os.startfile(r"Programm\terraform\terraform_destroy.ps1")
    for vm in vm_all:
        vm.running = False
        vm.save()

    with open("Programm/logs.txt", "a") as log_file:
        log_file.write(f"[{vm.time_update}] deleted all vm\n")
