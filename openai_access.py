import os
# Overwrite SSL_CERT_FILE from .env for this script to use system CA bundle, else openai.APIConnectionError: Connection error.
os.environ["SSL_CERT_FILE"] = "/etc/ssl/certs/ca-certificates.crt"
import os

from openai import OpenAI


client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
print(os.environ.get("SSL_CERT_FILE"))

models = client.models.list()

resp = client.responses.create(
    model="gpt-5-nano",  # models.data[0].id,
    input="Reply with exactly: OK"
)

print(resp.output_text)