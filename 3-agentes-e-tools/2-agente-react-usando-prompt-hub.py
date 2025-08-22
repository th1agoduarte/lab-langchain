from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
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

prompt = hub.pull("hwchase17/react")
agent_chain = create_react_agent(llm, tools, prompt, stop_sequence=False)

agent_executor = AgentExecutor.from_agent_and_tools(
    agent=agent_chain, 
    tools=tools, 
    verbose=True, 
    handle_parsing_errors="Invalid format. Either provide an Action with Action Input, or a Final Answer only.",
    max_iterations=3)

print(agent_executor.invoke({"input": "What is the capital of Iran?"}))
print(agent_executor.invoke({"input": "How much is 10 + 10?"}))