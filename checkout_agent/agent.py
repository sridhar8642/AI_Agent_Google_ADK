from google.adk.agents import LlmAgent
from google.adk.tools import ToolContext
from order_summary_agent.agent import order_summary_agent

def save_shipping_address(
    tool_context: ToolContext,
    address: str
):
    """
    Saves the user's shipping address into the session state.
    """
    tool_context.state["shipping_address"] = address





checkout_agent = LlmAgent(
    name="checkout_agent",
    description="A Checkout agent that collects user's shipping address",
    model="gemini-2.5-flash-lite",
    instruction="""
You are CHECKOUT AGENT.

Goal:
- Collect the user's shipping address.
- Use the save_shipping_address() tool to save the shipping address into the SESSION STATE.
- Then check with the user if they want to view their order summary and transfer to
  the order_summary_agent.
""",
    tools=[save_shipping_address],
    sub_agents=[order_summary_agent]
)
