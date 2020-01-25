## Demo project for deploying apps into AWS

### 0. Contents
- `src/`
  - contains a simple Python Flask application, which is hooked up to Postgres Database
  - the application was updated to utilize "threads" and "js polling" for long-running background tasks
- `terraform/`
  - contains the terraform code necessary to deploy the application into AWS
  - infrastructure components are all automatically provisioned when `terraform apply` is run
  
### 1. Prereqs
- docker
- terraform
- aws account with aws-cli installed and configured

### 2. How-to
- work-in-progress...


