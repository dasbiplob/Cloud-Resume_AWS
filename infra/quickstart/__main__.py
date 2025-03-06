import pulumi
import pulumi_aws as aws

# Reference the existing S3 bucket
website_bucket = aws.s3.Bucket.get("cloud-resume-biplob", "cloud-resume-biplob")

# Reference the existing DynamoDB table
dynamodb_table = aws.dynamodb.Table.get("cloudresume-test", "cloudresume-test")

# Set public access for the S3 bucket
public_access_block = aws.s3.BucketPublicAccessBlock("website_bucket",
    bucket=website_bucket.id,
    block_public_acls=False,
    block_public_policy=False,
    ignore_public_acls=False,
    restrict_public_buckets=False)

# Add a bucket policy to allow public read access
bucket_policy = aws.s3.BucketPolicy("public_read",
    bucket=website_bucket.id,
    policy=website_bucket.id.apply(lambda id: f"""
    {{
        "Version": "2012-10-17",
        "Statement": [
            {{
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::{id}/*"
            }}
        ]
    }}
    """))

# Reference the existing IAM role
lambda_role = aws.iam.Role.get("iam_for_lambda", "iam_for_lambda")

# Attach policies to the IAM role
lambda_policy = aws.iam.RolePolicy("iam_policy_for_resume_project",
    role=lambda_role.id,
    policy=dynamodb_table.arn.apply(lambda arn: f"""
    {{
        "Version": "2012-10-17",
        "Statement": [
            {{
                "Action": [
                    "logs:CreateLogGroup",
                    "logs:CreateLogStream",
                    "logs:PutLogEvents"
                ],
                "Resource": "*",
                "Effect": "Allow"
            }},
            {{
                "Effect": "Allow",
                "Action": [
                    "dynamodb:UpdateItem",
                    "dynamodb:GetItem"
                ],
                "Resource": "{arn}"
            }}
        ]
    }}
    """))

# Package the Lambda function code
lambda_zip = pulumi.FileArchive("../lambda/lambdaFunc.zip")

# Create the Lambda function
lambda_function = aws.lambda_.Function("myfunc",
    code=lambda_zip,
    role=lambda_role.arn,
    handler="lambdaFunc.lambda_handler",
    runtime="python3.8",
    environment={
        "variables": {
            "TABLE_NAME": dynamodb_table.name,
        }
    })

# Create a Lambda Function URL
lambda_url = aws.lambda_.FunctionUrl("url1",
    function_name=lambda_function.name,
    authorization_type="NONE",
    cors=aws.lambda_.FunctionUrlCorsArgs(
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["date", "keep-alive"],
        expose_headers=["keep-alive", "date"],
        max_age=86400,
    ))

# Export the Lambda Function URL
pulumi.export("lambda_url", lambda_url.function_url)
