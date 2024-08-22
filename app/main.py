
import os
from dotenv import load_dotenv, find_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from graph import CalculatorGraph

_ = load_dotenv(find_dotenv())

openai_api_key = os.environ["OPENAI_API_KEY"]

llm = ChatOpenAI(
    api_key=openai_api_key,
    model="gpt-3.5-turbo"
)

system_message = SystemMessage(
    content="Eres una calculadora diseñada para resolver las operaciones básicas")

calculator_graph = CalculatorGraph(llm, system_message)
agent = calculator_graph.compile_graph()

initial_state = {"first_number": 0, "second_number": 0, "result": 0, "operation": 1}
agent.invoke(initial_state)
