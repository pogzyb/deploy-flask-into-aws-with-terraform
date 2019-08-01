/********
variables
*********/

variable "vpc_cidr" {
  description = "The CIDR Block for the SiteSeer VPC"
  default     = "10.0.0.0/16"
}

variable "rt_wide_route" {
  description = "Route in the SiteSeer Route Table"
  default     = "0.0.0.0/0"
}

variable "public_cidrs" {
  description = "Public Subnet CIDR Blocks"
  default = [
    "10.0.1.0/24",
    "10.0.2.0/24"
  ]
}

variable "private_cidrs" {
  description = "Public Subnet CIDR Blocks"
  default = [
    "10.0.3.0/24",
    "10.0.4.0/24"
  ]
}

variable "flask_app_port" {
  description = "Port exposed by the flask application"
  default = "8080"
}

variable "postgres_db_port" {
  description = "Port exposed by the RDS instance"
  default = "5432"
}

variable "rds_instance_type" {
  description = "Instance type for the RDS database"
  default = "db.t2.micro"
}