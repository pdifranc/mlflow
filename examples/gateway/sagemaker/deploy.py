from sagemaker.jumpstart.model import JumpStartModel

model_id = "meta-textgeneration-llama-2-7b-f"
my_model = JumpStartModel(model_id=model_id)

predictor = my_model.deploy(instance_type='ml.g5.2xlarge')

print(f"endpoint_name = {my_model.endpoint_name}")
