class Agent:
    def __init__(self, name, role, goal):
        self.name = name
        self.role = role
        self.goal = goal

    def act(self, observation):
        """
        Simple agentic behavior: respond based on role and goal.
        """
        return (
            f"[{self.name} - {self.role}] My goal is: {self.goal}. "
            f"I observed: '{observation}'. I will take action accordingly."
        )

if __name__ == "__main__":
    # Example usage
    agent = Agent(
        name="Alice",
        role="Research Assistant",
        goal="Summarize scientific articles efficiently."
    )
    observation = "Received a new article on quantum computing."
    print(agent.act(observation))
