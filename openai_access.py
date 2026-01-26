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


# =============================================================
# MassBank Tool Integration Example
# =============================================================
from tools import MassBankTool

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
    try:
        compound_name = "Telmisartan O-acyl-glucuronide"
        print(f"Querying mass for compound name: {compound_name} ...")
        mass = query_mass_of_compound_by_name(compound_name)
        print(f"Mass of {compound_name}: {mass}")
    except Exception as e:
        print("MassBank tool integration failed:", e)
