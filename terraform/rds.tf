/********

terraform/prereqs/rds.tf contains all the necessary resources to
setup the RDS postgres database for the ECS application

Resources:
- Application Load Balancer
- AWS RDS Database (Postgres)
- Security Groups

*********/

# create the RDS instance
resource "aws_db_instance" "fp-rds" {
  allocated_storage    = 20
  storage_type         = "gp2"
  engine               = "postgres"
  engine_version       = "11"
  instance_class       = "db.t2.micro"
  name                 = ""
  username             = ""
  password             = ""
  parameter_group_name = ""
  db_subnet_group_name = aws_db_subnet_group.fp-db-subnet.name
}

# create security group
resource "aws_security_group" "rds-db-sg" {
  name = "postgres-security-group"
  vpc_id = aws_vpc.fp-vpc.id

  # Only postgres in
  ingress {
    from_port = var.postgres_db_port
    to_port = var.postgres_db_port
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port = 0
    to_port = 0
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}