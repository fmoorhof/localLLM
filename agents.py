import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama

load_dotenv()

class Agent:
    def __init__(self, name, role, goal, model="qwen3:30b-a3b"):
        self.name = name
        self.role = role
        self.goal = goal
        self.model = model
        self.base_url = os.environ["CUSTOM_BASE_URL"]
        self.api_key = os.environ["OPENWEBUI_SECRET_KEY"]
        self.llm = ChatOllama(
            model=self.model,
            base_url=self.base_url,
            client_kwargs={
                "headers": {"Authorization": f"Bearer {self.api_key}"},
            },
        )

    def act(self, observation):
        """
        Respond based on role, goal, and observation, using the LLM.
        """
        prompt = (
            f"You are {self.name}, a {self.role}. "
            f"Your goal is: {self.goal}. "
            f"Observation: {observation}\n"
            f"What should you do next?"
        )
        response = self.llm.predict(text=prompt)
        return response

if __name__ == "__main__":
    # Example usage
    agent = Agent(
        name="Alice",
        role="Research Assistant",
        goal="Summarize scientific articles efficiently."
    )
    observation = "Paste your article here that should be summarized."
    print(agent.act(observation))
