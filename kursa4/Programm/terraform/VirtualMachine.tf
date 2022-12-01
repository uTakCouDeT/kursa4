terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  service_account_key_file = "key.json"
  cloud_id                 = "b1g8utq2rgtdkf7tbuvi"
  folder_id                = "b1gqet1vvht76ltlvbgf"
  zone                     = "ru-central1-a"
}

resource "yandex_vpc_network" "network" {
  name = "network"
}

resource "yandex_vpc_subnet" "subnet" {
  name           = "subnet1"
  zone           = "ru-central1-a"
  network_id     = yandex_vpc_network.network.id
  v4_cidr_blocks = ["192.168.10.0/24"]
}

resource "yandex_compute_instance" "vm-1" {
  name        = "terraform"
  description = ""
  resources {
    core_fraction = 20
    cores         = 2
    memory        = 2
  }
  boot_disk {
    device_name = "ubunta"
    initialize_params {
      image_id = "fd8iajirduaku7taq42a"
      type     = "network-hdd"
      size     = 15
    }
  }
  network_interface {
    subnet_id = yandex_vpc_subnet.subnet.id
    nat       = true
  }
  metadata = {
    user-data = file("meta.txt")
  }
  service_account_id = "ajecupuvdpp99gv58j84"
}

output "internal_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.ip_address
}

output "external_ip_address_vm_1" {
  value = yandex_compute_instance.vm-1.network_interface.0.nat_ip_address
}
