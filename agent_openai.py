class MinimalOpenAIAgent:
    def __init__(self, client, model):
        self.client = client
        self.model = model

    def act(self, observation):
        prompt = f"You are an assistant. Observation: {observation}"
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content



if __name__ == "__main__":
    import os
    # Overwrite SSL_CERT_FILE from .env for this script to use system CA bundle, else openai.APIConnectionError: Connection error.
    os.environ["SSL_CERT_FILE"] = "/etc/ssl/certs/ca-certificates.crt"
    import os

    from openai import OpenAI
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    model = "gpt-5-nano"
    try:
        agent = MinimalOpenAIAgent(client, model)
        observation = "List three benefits of regular exercise."
        answer = agent.act(observation)
        print("MinimalOpenAIAgent answer:", answer)
    except Exception as e:
        print("MinimalOpenAIAgent failed:", e)