# resource "google_compute_instance" "airflow_vm_instance" {
#   name                      = "airflow-instance"
#   machine_type              = "e2-standard-2"
#   zone                      = var.zone
#   allow_stopping_for_update = true

#   boot_disk {
#     initialize_params {
#       image = var.vm_image
#       size  = 30
#     }
#   }

#   network_interface {
#     network = var.network
#     access_config {
#     }
#   }
# }