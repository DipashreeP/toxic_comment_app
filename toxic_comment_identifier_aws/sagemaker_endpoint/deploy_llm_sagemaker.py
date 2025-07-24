import sagemaker
from sagemaker.huggingface import HuggingFaceModel

# Get SageMaker execution role
role = sagemaker.get_execution_role()

# Define the HuggingFace Model Hub configuration
hub = {
    'HF_MODEL_ID': 'google/flan-t5-small',
    'HF_TASK': 'text2text-generation'
}

# Create HuggingFace Model object
huggingface_model = HuggingFaceModel(
    transformers_version='4.26.0',
    pytorch_version='1.13.1',
    py_version='py39',
    env=hub,
    role=role
)

# Deploy the model to a SageMaker endpoint (Free Tier eligible instance)
predictor = huggingface_model.deploy(
    initial_instance_count=1,
    instance_type='ml.t2.medium'  # Free Tier eligible
)

print('SageMaker endpoint deployed! Endpoint name:', predictor.endpoint_name) 