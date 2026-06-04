import boto3
import json

client=boto3.client(
    'bedrock-runtime',
    region_name="us-east-1"
)

model_id="anthropic.claude-3-sonnet-20240229-v1:0"

body = {
"anthropic_version": "bedrock-2023-05-31",
"max_tokens": 200,
"temperature": 1,
"messages": [
{
"role": "user",
"content": [
{
"type": "text",
"text": "Write a leave application email"
}
]
}
]
}


response=client.invoke_model(
    modelId=model_id,
    body=json.dumps(body)
)

response_text=json.loads(response["body"].read())
text=response_text["content"][0]["text"]


for line in text.split("\n"):
    print(line)