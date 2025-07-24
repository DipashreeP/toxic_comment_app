#!/bin/bash

# Exit on error
set -e

# 1. Initialize Elastic Beanstalk application
# (Assumes you are in the webapp directory)
eb init -p python-3.9 toxic-comment-webapp --region us-east-1

# 2. Set environment variables (replace with your actual values)
eb setenv SAGEMAKER_ENDPOINT=your-endpoint-name AWS_REGION=us-east-1

# 3. Create and deploy the environment
eb create toxic-comment-env

# 4. Open the deployed app in the browser
eb open 