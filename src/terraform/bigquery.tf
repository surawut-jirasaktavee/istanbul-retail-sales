# DWH
# Ref: https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset
resource "google_bigquery_dataset" "stg_dataset" {
  dataset_id                 = var.stg_bq_dataset
  project                    = local.project_id
  location                   = local.region
  delete_contents_on_destroy = true
  labels                     = local.common_tags
}

resource "google_bigquery_dataset" "prod_dataset" {
  dataset_id                 = var.prod_bq_dataset
  project                    = local.project_id
  location                   = local.region
  delete_contents_on_destroy = true
  labels                     = local.common_tags
}