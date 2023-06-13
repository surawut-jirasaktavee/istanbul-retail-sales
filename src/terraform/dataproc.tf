# resource "google_dataproc_cluster" "multinode_spark_cluster" {
#   name   = "multinode-spark-cluster"
#   region = local.region

#   cluster_config {

#     staging_bucket = var.bucket

#     gce_cluster_config {
#       network = var.network
#       zone    = var.zone

#       shielded_instance_config {
#         enable_secure_boot = true
#       }
#     }

#     master_config {
#       num_instances = 1
#       machine_type  = "e2-standard-2"
#       disk_config {
#         boot_disk_type    = "pd-ssd"
#         boot_disk_size_gb = 30
#       }
#     }

#     worker_config {
#       num_instances = 2
#       machine_type  = "e2-medium"
#       disk_config {
#         boot_disk_size_gb = 30
#       }
#     }

#     software_config {
#       image_version = "2.0-debian10"
#       override_properties = {
#         "dataproc:dataproc.allow.zero.workers" = "true"
#       }
#       optional_components = ["JUPYTER"]
#     }
#   }

# }