# Project to build and deploy Web Application on containers with CICD and Terraform

# Primary tools chosen to achieve the project requirements are as follows:

# 1. CICD - Github Actions workflow
# 2. Containers - AWS ECR for docker image repository and  AWS ECS Fargate to deploy containers.
# 3. Infrastructure provisioning - Terraform
# 4. Code repository - Github

# Pre-requisites

# 1. You will need docker installed in your environment
# 2. You will also need Postman to test API endpoints
# 3. You will need to install PostgreSQL and pgAdmin to test RDS connection

# Step 1 - Clone Repo to your local environment

#  - Run  git clone https://github.com/evannoelchi/python-webapp-peach.git

# Step 2 - Provision resources on AWS with Terraform

# - Access terraform files run command - 'cd terraform' from project directory
# - Run terraform commands to bring up the infrastructure - terraform init, 
#   terraform plan, terraform apply.
# - RDS, ECR, ECS and ALB should be ready after this
#   (NB: Take note of outputs after running terraform cmds for important details about the       infrastructure )
# - Edit Inbound rules for RDS security group to Allow All TCP traffic.
# - Create connection with RDS in pgAdmin and test connection to DB, make sure connection is successful. 

# Step 3 - Run Github Actions workflow to build and deploy container to ECS

# - If there is a git push to the main branch the workflow automatically build and deploy the container image to ECS.
# - GH Actions will show the processes of the deployment inorder

# Step 4 - Test the application using Postman

# - To create a new user, make a POST request at the endpoint /users
# - To get a single user, make a GET request, appending the id of the user we want to retrieve at the end of the /users path. For example /users/2 retrieves the user with id = 2.
# - To update an existing user, make a PUT request. Specify the id of the user we want to modify in the url and the new user in the body of the request.
# - Finally, to delete an existing user - for example, the user with id = 3 - we can make a DELETE quest at the path /users/3

# Step 5 - Destroy the resources
# - Delete container image in ECR in AWS Console.
# - Run terraform destroy -auto-approve . This will then destroy all the provisioned resources.

# Future improvements to consider

# - Intergrate a GH Actions workflow that automatically provisions the terraform files.
# - Define VPC, subnets and security group CIDR parameters instead of using defaults
# - Deploy containers on AWS EKS instead of ECS

# Thank you!!!!
