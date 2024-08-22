"""Main """

import os
from typing import TypedDict
from langchain_core.messages import SystemMessage
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

from nodes.nodes import get_first_number_node, get_result_node, get_second_number_node

from constants.constanst import GET_FIRST_NUMBER_NODE, GET_RESULT_NODE, GET_SECOND_NUMBER_NODE

_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

llm = ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model="gpt-3.5-turbo"
)

system_message = SystemMessage(
    content="You are a calculator designed to solve basic operations")


class State(TypedDict):
    first_number: int
    second_number: int
    result: int


workflow = StateGraph(State)

workflow.add_node(GET_FIRST_NUMBER_NODE, lambda state: get_first_number_node(
    state, llm, system_message))
workflow.add_node(GET_SECOND_NUMBER_NODE, lambda state: get_second_number_node(
    state, llm, system_message))
workflow.add_node(GET_RESULT_NODE, get_result_node)

workflow.set_entry_point(GET_FIRST_NUMBER_NODE)

workflow.add_edge(GET_FIRST_NUMBER_NODE, GET_SECOND_NUMBER_NODE)
workflow.add_edge(GET_SECOND_NUMBER_NODE, GET_RESULT_NODE)
workflow.add_edge(GET_RESULT_NODE, END)

agent = workflow.compile()

initial_state = {"first_number": 0, "second_number": 0, "result": "1"}
agent.invoke(initial_state)
