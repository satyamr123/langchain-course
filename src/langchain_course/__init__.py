#python -u "c:\Users\satya\Documents\GitHub\langchain-course\src\langchain_course\__init__.py"
from dotenv import load_dotenv
#from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from langchain.tools import tool
from tavily import TavilyClient

load_dotenv()
tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Tool that searches over internet
    Args:
        query: the query to search for
    Returns:
        The search result 
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

llm = ChatOpenAI()
tools = [search]
agent = create_agent(model = llm, tools=tools)

def main():
    print("Hi this is me")
    result = agent.invoke({"messages":HumanMessage(content="What is the weather in Tokyo")})
    print(result)
    pass

if __name__ == "__main__":
    main()