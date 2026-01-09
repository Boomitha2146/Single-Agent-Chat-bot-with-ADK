from google.adk.agents.llm_agent import Agent
from google.adk.runners import Runner

# Create the agent
root_agent = Agent(
    name="single_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful AI assistant."
)

# Create runner (THIS executes the agent)
runner = Runner(root_agent)

def run(user_input: str):
    """Run the ADK agent and return the response"""
    response = runner.run(user_input)
    return response
