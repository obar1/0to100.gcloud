terraform {
  required_providers {
    google = {
      version = "3.90.1"
    }
    google-beta = {
      version = "3.90.1"
    }
  }
}

provider "google" {
  project = var.project_id
  region  = var.project_region
}

provider "google-beta" {
}

provider "null" {
}

provider "random" {
}

resource "random_id" "name" {
  byte_length = 2
}

resource "random_id" "pass" {
  byte_length = 16
}