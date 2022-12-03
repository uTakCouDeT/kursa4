from MySite.models import VirtualMachine
import os


def create_vm_template(vm_name):
    with open("Programm/terraform/VirtualMachine.tf", "a") as tf_file:
        with open("Programm/template.txt") as tmpl:
            tf_file.write('\n' + tmpl.read())


def delete_vm_template(vm_name):
    with open("Programm/terraform/VirtualMachine.tf") as tf_file:
        text = tf_file.readlines()
        for i in range(len(text)):
            if text[i] == "resource \"yandex_compute_instance\" \"vm-1\" {\n":
                with open("Programm/terraform/VirtualMachine.tf", "w") as tf_file:
                    tf_file.writelines(text[:i - 1] + text[i + 32:])
                break


def run_terraform_apply_and_change_running_flag(vm):
    # os.startfile("Programm/terraform/terraform_apply.ps1")
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
    # os.startfile("Programm/terraform/terraform_destroy.ps1")
    for vm in vm_all:
        vm.running = False
        vm.save()

    with open("Programm/logs.txt", "a") as log_file:
        log_file.write(f"[{vm.time_update}] deleted all vm\n")
