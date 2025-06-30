# IAM Role to S3 Access Validation

This repo is a test validation project where I simulated how an EC2 instance can securely access an S3 bucket using an IAM Role and temporary credentials via STS — no hardcoded keys, no user-based access, just clean, scoped permissions the way AWS recommends it.

## What This Shows

- IAM Role with a trust policy allowing EC2 to assume it
- Inline policy that only gives access to one specific S3 bucket (least privilege)
- EC2 launched with that role attached
- A Python script using `boto3` to confirm the EC2 has valid STS-based access

## Why It Matters

This reflects real-world cloud engineering practices:

- You should never hardcode access keys into EC2
- Roles are the secure way to let services talk to each other
- Temporary credentials via STS reduce long-term risk
- This setup is the baseline for secure automation, pipelines, and internal tools 
