import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

base_url = os.environ["CUSTOM_BASE_URL"]  # defined in .env file
api_key = os.environ["OPENWEBUI_SECRET_KEY"]

# verify that environment variables are loaded correctly
print(f"Base URL: {base_url}")
print(f"API Key: {api_key}")
print(f"SSL_CERT_FILE: {os.environ.get('SSL_CERT_FILE')}")


client = ChatOllama(
    model="qwen3:30b-a3b",
    base_url=base_url,
    client_kwargs={  # httpx ssl authentication
        "headers": {
            "Authorization": f"Bearer {api_key}",
        },
    },
    # + .env file needs to contain the path to SSL_CERT_FILE when using corporate hosted chatbot
    )

response = client.predict(text="What is the capital of France?")
print(response)
