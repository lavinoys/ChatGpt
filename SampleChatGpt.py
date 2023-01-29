import openai

# Apply the API key
openai.api_key = "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"

# Define the prompt
prompt = "Hello, I am a language model. How can I help you today?"

# Generate a response
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the response
print(response["choices"][0]["text"])
