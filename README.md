Chicken Disease Classification Project
Workflows

Update config.yaml

Update secrets.yaml [Optional]

Update params.yaml

Update the entity

Update the configuration manager in src/config

Update the components

Update the pipeline

Update main.py

Update the dvc.yaml

How to run?
Steps

Clone the repository

git clone https://github.com/nisha132/Chicken_DiseseClassification.git
cd Chicken_DiseseClassification


STEP 01 - Create a conda environment after opening the repository

conda create -n cnncls python=3.8 -y
conda activate cnncls


STEP 02 - Install the requirements

pip install -r requirements.txt


STEP 03 - Run the application

python app.py


Now open up your local host and port in the browser.

DVC Commands

dvc init

dvc repro

dvc dag

AWS CI/CD Deployment with GitHub Actions
1. Login to AWS console.
2. Create IAM user for deployment

With specific access:

EC2 access: Virtual machine

ECR access: Elastic Container Registry (to store docker images)

Description of deployment:

Build docker image of the source code

Push docker image to ECR

Launch EC2

Pull docker image from ECR in EC2

Run docker container in EC2

Policies required:

AmazonEC2ContainerRegistryFullAccess

AmazonEC2FullAccess

3. Create ECR repo to store/save docker image

👉 Save the repository URI for later use. Example:

<aws-account-id>.dkr.ecr.<region>.amazonaws.com/chicken

4. Create EC2 machine (Ubuntu)
5. Install Docker in EC2
sudo apt-get update -y
sudo apt-get upgrade -y

# install docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker ubuntu
newgrp docker

6. Configure EC2 as self-hosted runner

Navigate to:
GitHub repo → Settings → Actions → Runners → New self-hosted runner → choose OS → follow setup commands

7. Setup GitHub secrets

Configure the following in your repo → Settings → Secrets and variables → Actions:

AWS_ACCESS_KEY_ID = <your-aws-access-key>
AWS_SECRET_ACCESS_KEY = <your-aws-secret-key>
AWS_REGION = <your-region>
AWS_ECR_LOGIN_URI = <aws-account-id>.dkr.ecr.<region>.amazonaws.com
ECR_REPOSITORY_NAME = <your-repository-name>
