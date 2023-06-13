# resource "google_compute_firewall" "port_rules" {
#   project     = local.project_id
#   name        = "kafka-broker-port"
#   network     = var.network
#   description = "Opens port 9092 in the Kafka VM for Spark cluster to connect"

#   allow {
#     protocol = "tcp"
#     ports    = ["9092"]
#   }

#   source_ranges = ["0.0.0.0/0"] # The firewall rule applies to all IP addresses
#   target_tags   = ["kafka"]     # The rule is applied only to instances that have the "kafka" tag

# }

# resource "google_compute_instance" "kafka_vm_instance" {
#   name                      = "kafka-instance"
#   machine_type              = "e2-standard-2"
#   tags                      = ["kafka"]
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