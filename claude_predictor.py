import anthropic

client = anthropic.Anthropic(
    api_key="your_api_key"  # Replace with your real key or set as env variable
)

message = client.messages.create(
    model="claude-3.5-sonnet-20240627",  # ✅ Correct model ID
    max_tokens=1000,
    temperature=1,
    messages=[
        {"role": "user", "content": "What is the capital of France?"}
    ]
)

print(message.content[0].text)
