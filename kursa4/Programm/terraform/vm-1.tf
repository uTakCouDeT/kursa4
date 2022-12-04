resource "yandex_vpc_subnet" "subnet_vm-1" {
  name           = "subnet_vm-1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

resource "yandex_compute_instance" "vm-1" {
  name        = "vm-1"
  description = "description-1"
  resources {
    core_fraction = 20
    cores         = 2
    memory        = 2
  }
  boot_disk {
    initialize_params {
      image_id = "fd8phu675e6sgsa68pvj"
      type     = "network-hdd"
      size     = 15
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet_vm-1.id
    nat       = true
  }
  metadata = {
    user-data = file("meta_vm-1.txt")
  }
  service_account_id = "ajecupuvdpp99gv58j84"
}

output "internal_ip_address_vm-1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "external_ip_address_vm-1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}
