from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

@tool("calculator", return_direct=True)
def calculator_tool(expresion: str) -> str:
    """Evaluate a simple mathematical expression and return the result."""
    try:
        result = eval(expresion) #be careful with this because it`s a security risk if the input is not controlled`
    except Exception as e:
        return f"Error: {str(e)}"

    return str(result)

@tool("web_search_mock")
def web_search_mock(query: str) -> str:
    """Mock web search tool that returns a fixed response."""
    # country capitals data
    # In a real-world scenario, this would perform an actual web search.
    # Here, we will use a predefined dictionary of country capitals.
    data = {
        "Brazil": "Brasília",
        "Argentina": "Buenos Aires",
        "United States": "Washington, D.C.",
        "France": "Paris",
        "Germany": "Berlin",
        "Japan": "Tokyo",
        "China": "Beijing",
        "India": "New Delhi",
        "Russia": "Moscow",
        "Canada": "Ottawa",
        "Australia": "Canberra",
        "Italy": "Rome",
        "Spain": "Madrid",
        "United Kingdom": "London",
        "South Africa": "Pretoria",
        "Mexico": "Mexico City",
        "South Korea": "Seoul",
        "Netherlands": "Amsterdam",
        "Sweden": "Stockholm",
        "Norway": "Oslo",
        "Finland": "Helsinki",
        "Denmark": "Copenhagen",
        "Belgium": "Brussels",}
    
    for country, capital in data.items():
        if country.lower() in query.lower():
            return f"The capital of {country} is {capital}."

    return "Sorry, I couldn't find the capital for that country."

llm = ChatOpenAI(model="gpt-5-mini", disable_streaming=True)
tools = [calculator_tool, web_search_mock]
prompt = PromptTemplate.from_template(
"""
Answer the following questions as best you can. You have access to the following tools.
Only use the information you get from the tools, even if you know the answer.
If the information is not provided by the tools, say you don't know.

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action

... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Rules:
- If you choose an Action, do NOT include Final Answer in the same step.
- After Action and Action Input, stop and wait for Observation.
- Never search the internet. Only use the tools provided.

Begin!

Question: {input}
Thought:{agent_scratchpad}"""
)
agent_chain = create_react_agent(llm, tools, prompt, stop_sequence=False)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent_chain, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors="Invalid format. Either provide an Action with Action Input, or a Final Answer only.",
    max_iterations=3)

print(agent_executor.invoke({"input": "What is the capital of Iran?"}))
print(agent_executor.invoke({"input": "How much is 10 + 10?"}))