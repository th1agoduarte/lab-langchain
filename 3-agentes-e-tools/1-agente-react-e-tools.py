from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

@tool("calculator", return_direct=True ,description="A simple calculator that can evaluate basic mathematical expressions.")
def calculator_tool(expresion: str) -> str:
    """Evaluate a simple mathematical expression and return the result."""
    try:
        result = eval(expresion) #be careful with this because it`s a security risk if the input is not controlled`
    except Exception as e:
        return f"Error: {str(e)}"

    return str(result)

@tool("web_search_mock", description="A simple web search tool that can search the web for information.")
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