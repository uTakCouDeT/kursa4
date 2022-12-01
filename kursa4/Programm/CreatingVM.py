from MySite.models import VirtualMachine


def CreateVirtualMachine(vm_name):
    with open("Programm/terraform/VirtualMachine.tf", "a") as tf_file:
        vm = VirtualMachine.objects.get(name=vm_name)
        with open("Programm/template.txt") as tmpl:
            tf_file.write('\n' + tmpl.read())

    #

    vm.running = True
    vm.save()

    with open("Programm/logs.txt", "a") as log_file:
        log_file.write(f"[{vm.time_update}] created vm: {vm.name}\n")


def DeleteVirtualMachine(vm_name):
    with open("Programm/terraform/VirtualMachine.tf") as tf_file:
        text = tf_file.readlines()
        for i in range(len(text)):
            if text[i] == "resource \"yandex_compute_instance\" \"vm-1\" {\n":
                vm_index = i - 1
                break

    with open("Programm/terraform/VirtualMachine.tf", "w") as tf_file:
        vm = VirtualMachine.objects.get(name=vm_name)
        tf_file.writelines(text[0:vm_index])

    #

    vm.running = False
    vm.save()

    with open("Programm/logs.txt", "a") as log_file:
        log_file.write(f"[{vm.time_update}] deleted vm: {vm.name}\n")
