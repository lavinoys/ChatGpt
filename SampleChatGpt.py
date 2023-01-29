import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Apply the API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# specify the prompt
prompt = "Write a Python function to print the first n Fibonacci numbers."

# generate code
completions = openai.Completion.create(
    engine="code-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# get the first response
message = completions.choices[0].text

# print the response
print(message)
