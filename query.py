import os
import httpx

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

from tools import MassBankTool

load_dotenv()

base_url = os.environ["CUSTOM_BASE_URL"]  # defined in .env file
api_key = os.environ["OPENWEBUI_SECRET_KEY"]

# verify that environment variables are loaded correctly
print(f"Base URL: {base_url}")
print(f"API Key: {api_key}")
print(f"SSL_CERT_FILE: {os.environ.get('SSL_CERT_FILE')}")


# Discover available models from Ollama
with httpx.Client(base_url=base_url, headers={"Authorization": f"Bearer {api_key}"}, timeout=15.0) as s:
    resp = s.get("/api/tags")
    resp.raise_for_status()
    models = [m.get("name") for m in resp.json().get("models", [])]
print(f"Available models: {models}")


# Chat with an Ollama model
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


# --- MassBank tool integration example ---
def query_mass_of_compound_by_name(compound_name):
    tool = MassBankTool(verify_ssl=False)
    endpoint = "/records"
    params = {"compound_name": compound_name}
    try:
        result = tool.call_api(endpoint, params=params)
        # Try to extract mass from the first record, if available
        if isinstance(result, list) and result:
            record = result[0]
            # Mass is usually under record['compound']['mass']
            mass = record.get("compound", {}).get("mass")
            return mass if mass else f"Mass not found in first record: {record}"
        return f"No records found for compound: {compound_name}"
    except Exception as e:
        return f"Error querying MassBank: {e}"

if __name__ == "__main__":
    compound_name = "Telmisartan O-acyl-glucuronide"  # MSBNK-IPB_Halle-PB001341
    print(f"Querying mass for compound name: {compound_name} ...")
    mass = query_mass_of_compound_by_name(compound_name)
    print(f"Mass of {compound_name}: {mass}")
    