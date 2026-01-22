import httpx


class MassBankTool:
    """
    Universal tool to interact with the MassBank3 API (https://msbi.ipb-halle.de/MassBank3-api/ui/openapi.json).
    This tool can be used by an LLM agent to call any endpoint with arbitrary parameters.
    """
    BASE_URL = "https://msbi.ipb-halle.de/MassBank3-api"

    def __init__(self, verify_ssl=True):
        self.verify_ssl = verify_ssl

    def call_api(self, endpoint: str, method: str = "GET", params: dict = None, json: dict = None):
        url = f"{self.BASE_URL}{endpoint}"
        with httpx.Client(timeout=15.0, verify=self.verify_ssl) as client:
            if method.upper() == "GET":
                resp = client.get(url, params=params)
            elif method.upper() == "POST":
                resp = client.post(url, params=params, json=json)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            resp.raise_for_status()
            return resp.json()

if __name__ == "__main__":
    tool = MassBankTool(verify_ssl=False)
    # Example: list available API endpoints (if supported by API)
    try:
        result = tool.call_api("/ui/openapi.json")
        print("OpenAPI spec keys:", list(result.keys()))
    except Exception as e:
        print("Error calling /openapi.json:", e)
