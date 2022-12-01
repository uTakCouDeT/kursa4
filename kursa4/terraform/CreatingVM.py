from MySite.models import VirtualMachine


def CreateVirtualMachine(vm_name):
    tf_file = open("terraform/aboba.txt", "w")

    vm = VirtualMachine.objects.get(name=vm_name)
    vm.running = True
    vm.save()
    tf_file.write("created " + vm.name)

    tf_file.close()


def DeleteVirtualMachine(vm_name):
    tf_file = open("terraform/aboba.txt", "w")

    vm = VirtualMachine.objects.get(name=vm_name)
    vm.running = False
    vm.save()
    tf_file.write("deleted " + vm.name)

    tf_file.close()
