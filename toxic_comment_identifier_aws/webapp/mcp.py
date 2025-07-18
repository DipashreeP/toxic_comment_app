import boto3
import json
import os

SAGEMAKER_ENDPOINT = os.environ.get('SAGEMAKER_ENDPOINT')
REGION = os.environ.get('AWS_REGION', 'us-east-1')
sm_runtime = boto3.client('sagemaker-runtime', region_name=REGION)

def process_comment(comment):
    prompt = (
        "You are an assistant that rewrites software/code-related comments to be neutral, professional, and respectful. "
        "Remove any insults, offensive language, or toxicity, but keep all technical meaning and intent. "
        "Do not add unrelated information or change the topic. Only rephrase the original comment in a more respectful way.\n"
        f"Original: {comment}\nRewritten:"
    )
    payload = {"inputs": prompt}
    response = sm_runtime.invoke_endpoint(
        EndpointName=SAGEMAKER_ENDPOINT,
        ContentType='application/json',
        Body=json.dumps(payload)
    )
    result = json.loads(response['Body'].read())
    rewritten = result[0]['generated_text'] if isinstance(result, list) else result
    return rewritten 