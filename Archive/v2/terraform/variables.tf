variable "access_key" {}
variable "secret_key" {}
variable "ssh_key_name" {}
variable "ssh_key_pub" {}
variable "vpc_id" {}
variable "bastion_subnet_id" {}
variable "region" {
  default = "us-east-2"
}

variable "availability_zones" {
  type = "map"
  default = {
    "us-east-2" = [
        "us-east-2a",
        "us-east-2b",
        "us-east-2c"
    ]
  }
}

variable "amis" {
  type = "map"
  default = {
    "us-east-2" = "ami-0a80c1bfc488c6673"
  }
}
