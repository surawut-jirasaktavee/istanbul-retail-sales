terraform {
  required_version = ">= 1.4.0"
  backend "local" {} # Can change from "local" to "gcs" (for google) or "s3" (for aws), if you would like to preserve your tf-state online
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = ">=4.6.0"
    }
  }
}
