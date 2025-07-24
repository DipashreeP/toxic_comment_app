import boto3
import json

# Replace with your actual SageMaker endpoint name and region
SAGEMAKER_ENDPOINT = 'huggingface-pytorch-inference-2025-07-18-13-21-54-787'
REGION = 'us-east-1'

# Test prompts
test_prompts = [
    "What a piece of crap. Only an idiot would write such garbage code.",
    "You must be the dumbest person to think this library is useful. Just quit coding forever.",
    "This is the worst implementation I've ever seen. Did you even test it?",
    "Your code is trash.",
    "Wow, did you even try to make this work, or was it just for fun?",
    "I think this code could be improved by adding more comments."
]

# Create SageMaker runtime client
sm_runtime = boto3.client('sagemaker-runtime', region_name=REGION)

for prompt in test_prompts:
    # You may need to format the prompt as your model expects (with instructions/examples)
    payload = {
        "inputs": f"Rewrite the following comment to be neutral, professional, and respectful, keeping the technical meaning. Remove any insults, offensive language, or toxicity. Do not add unrelated information or change the topic. Only rephrase the original comment in a more respectful way.\nOriginal: {prompt}\nRewritten:"
    }
    response = sm_runtime.invoke_endpoint(
        EndpointName=SAGEMAKER_ENDPOINT,
        ContentType='application/json',
        Body=json.dumps(payload)
    )
    result = json.loads(response['Body'].read())
    rewritten = result[0]['generated_text'] if isinstance(result, list) else result
    print(f"Original: {prompt}")
    print(f"Rewritten: {rewritten}\n{'-'*60}\n")