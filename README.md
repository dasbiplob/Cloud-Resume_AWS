# Cloud Resume Challenge - AWS

This project is part of the **Cloud Resume Challenge**, showcasing a static website hosted on AWS with a visitor counter. The website is built using AWS services like S3, CloudFront, Route 53, AWS Lambda, API Gateway, and DynamoDB. The infrastructure is automated using **Terraform** or **Pulumi**, and the deployment is managed via **GitHub Actions**.

---

## Features

- **Static Website**: Hosted on AWS S3, secured with AWS Certificate Manager (ACM), and delivered via CloudFront for global acceleration.
- **Visitor Counter**: A serverless visitor counter built with:
  - **AWS Lambda** (Python): Handles the logic for incrementing and retrieving the visitor count.
  - **API Gateway**: Exposes the Lambda function as a REST API.
  - **DynamoDB**: Stores the visitor count.
- **Automated Deployment**:
  - Infrastructure as Code (IaC) using **Terraform** or **Pulumi**.
  - Continuous Integration and Continuous Deployment (CI/CD) using **GitHub Actions**.

---

## Architecture Diagram

Here’s a high-level architecture of the project:



---

## Technologies Used

### AWS Services

- **S3**: Hosts the static website.
- **CloudFront**: Accelerates content delivery and provides HTTPS via ACM.
- **Route 53**: Manages DNS routing.
- **AWS Lambda**: Serverless function to handle visitor count logic.
- **API Gateway**: Exposes the Lambda function as a REST API.
- **DynamoDB**: Stores the visitor count.
- **Certificate Manager (ACM)**: Provides SSL/TLS certificates for HTTPS.

### Infrastructure as Code (IaC)

- **Terraform** or **Pulumi**: Automates the provisioning of AWS resources.

### CI/CD

- **GitHub Actions**: Automates testing and deployment.

### Programming Languages

- **Python**: Lambda function logic.
- **HTML/CSS/JavaScript**: Static website content.

---

## Setup Instructions

### Prerequisites

1. **AWS Account**: Ensure you have an AWS account with the necessary permissions.
2. **GitHub Repository**: Fork or clone this repository.
3. **Terraform/Pulumi**: Install Terraform or Pulumi CLI on your local machine.
4. **Python**: Install Python 3.8 or later.

### Steps to Deploy

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/cloud-resume-challenge.git
cd cloud-resume-challenge

2. Set Up AWS Credentials
Configure your AWS credentials using the AWS CLI:

bash
Copy
aws configure
3. Initialize Terraform/Pulumi
For Terraform:

bash
Copy
cd infra/
terraform init
terraform apply
For Pulumi:

bash
Copy
cd infra/
pulumi stack select dev || pulumi stack init dev
pulumi up
4. Deploy Using GitHub Actions
Add the following secrets to your GitHub repository:

AWS_ACCESS_KEY_ID

AWS_SECRET_ACCESS_KEY

Push changes to the main branch to trigger the GitHub Actions workflow.

## Testing
Unit Tests
Run the unit tests for the Lambda function:

bash
Copy
cd lambda/
pip install -r requirements.txt
pytest test_api.py
Manual Testing
Visit the deployed website URL.

Verify that the visitor counter increments on each page load.
