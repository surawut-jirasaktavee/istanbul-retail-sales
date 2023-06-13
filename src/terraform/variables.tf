locals {
  common_tags = merge(jsondecode(file("${path.module}/common_tags.json")),
    {
      project_name = terraform.workspace
    }
  )
  project_id = "istanbul-retail-sales"
  region     = "asia-southeast1"
}

# variable "project" {
#   description = "Your GCP Project ID"
#   default     = "de-20230222"
#   type        = string
# }

# variable "region" {
#   description = "Region for GCP resources. Choose as per your location: https://cloud.google.com/about/locations"
#   default     = "asia-east1"
#   type        = string
# }

variable "storage_class" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default     = "STANDARD"
  type        = string
}

# variable "network" {
#   description = "Network for your instance/cluster"
#   default     = "default"
#   type        = string
# }

variable "zone" {
  description = "Your project zone"
  default     = "asia-southeast1-a"
  type        = string
}

# variable "vm_image" {
#   description = "Image for you VM"
#   default     = "ubuntu-os-cloud/ubuntu-2004-lts"
#   type        = string
# }

variable "stg_bq_dataset" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default     = "stg"
  type        = string
}

variable "prod_bq_dataset" {
  description = "Storage class type for your bucket. Check official docs for more info."
  default     = "prod"
  type        = string
}

variable "bucket" {
  description = "The name of your bucket. This should be unique across GCP"
  type        = string
  default     = "istanbul-retail-sales"
}