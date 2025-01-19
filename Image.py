import openai

openai.api_key = "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"

# Example usage:
response = openai.Image.create(prompt="A futuristic city", n=1, size="1024x1024")
print(response['data'][0]['url'])
