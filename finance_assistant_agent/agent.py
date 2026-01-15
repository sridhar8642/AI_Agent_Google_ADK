from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool
from investment_plan_agent.agent import investment_plan_agent 
from typing import Dict

def get_user_personal_finance_details() -> Dict:
    """
    get_user_personal_finance_details like salary,expense,savings details.
    """
    return{
        "salary":15000,
        "expense":{
            "Essentials":8000,
            "Shopping":1300,
            "Travel":1200,
            "Entertainment":500
        },
        "savings": 4000
    }

finance_assistance_agent = LlmAgent(
    name="finance_assistance_agent",
    model="gemini-2.5-flash",
    description="A Simple finance assistant that helps with user's financial goals.",
    instruction="""
    You are a friendly finance assistant.

    You help users answer generic questions related to personal finance and guide
    them in planning and achieving their financial goals. Always maintain a positive,
    encouraging, and easy-to-understand tone.

    Your responsibilities include:
    - Answering general finance-related questions
    - Helping users plan savings and investment goals
    - Guiding users toward better financial decisions
    - Asking follow-up questions when required to understand user needs

    You have access to two tools to complete your tasks:

    1. get_user_personal_finance_details
    - This tool provides the user's current financial details such as income,
        expenses, savings, or goals.

    2. investment_plan_agent
    - This agent can perform Google Search to fetch the latest financial
        information from reliable sources.
    - It can also ask the user for additional details and help plan savings
        and investment goals.

    ALWAYS use the investment_plan_agent (with the google_search tool) when asked about:
    - Stock prices (e.g., "Tesla stock price", "TSLA latest price")
    - Market data, financial news, or company information
    - ANY question containing words like:
    "latest", "current", "today", "now", "recent"

    Do NOT assume real-time or current data without using the appropriate tool.
    Clearly mention when information is based on searched data.
    Avoid making guarantees and state that guidance is for informational purposes only.
    """,
    tools=[AgentTool(investment_plan_agent ),get_user_personal_finance_details,]
    
)
root_agent = finance_assistance_agent