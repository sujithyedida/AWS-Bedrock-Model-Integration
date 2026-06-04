import boto3
import json

client=boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)
model_id="amazon.nova-lite-v1:0"
body = {
"messages": [
{
"role": "user",
"content": [{"text": "what is the significance of AI & ML"}]
}
],
"inferenceConfig": {
"maxTokens": 300,
"temperature": 0.5,
"topP": 0.9
}
}

response=client.invoke_model(
    modelId=model_id,
    body=json.dumps(body)
)

response_body=json.loads(response["body"].read())
print(response_body)