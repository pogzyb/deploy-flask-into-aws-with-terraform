/********

terraform/rds.tf contains all the necessary resources to
setup the RDS postgres database for the ECS application

Resources:
- Application Load Balancer
- AWS RDS Database (Postgres)
- Security Groups

*********/

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

# create the RDS instance
resource "aws_db_instance" "fp-rds" {
  allocated_storage           = 20
  storage_type                = "gp2"
  engine                      = "postgres"
  engine_version              = "11"
  instance_class              = var.rds_instance_type
  name                        = "postgresdb"
  username                    = "root"
  password                    = "admin123"
  port                        = var.postgres_db_port
  vpc_security_group_ids      = [aws_security_group.rds-db-sg.id]
  parameter_group_name        = "default.postgres11"
  db_subnet_group_name        = aws_db_subnet_group.fp-db-subnet.name
  publicly_accessible         = false
  allow_major_version_upgrade = false
  auto_minor_version_upgrade  = false
  apply_immediately           = true
  storage_encrypted           = false
}
