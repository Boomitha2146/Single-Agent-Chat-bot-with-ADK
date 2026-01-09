from google.adk.agents.llm_agent import Agent

# Create the agent
root_agent = Agent(
    model="gemini-2.5-flash",
    name="single_agent",
    instruction="You are a helpful AI assistant."
)

def run(user_input: str):
    """Run the agent with user input and return response"""
    result = root_agent.run(user_input)
    return result
