from langgraph.graph import StateGraph, END
from agent_node import CalculatorAgentNode
from constants.constanst import GET_FIRST_NUMBER_NODE, GET_SECOND_NUMBER_NODE, GET_RESULT_NODE
from state import CalculatorState


class CalculatorGraph:
    def __init__(self, llm, system_message):
        self.workflow = StateGraph(CalculatorState)
        self.calculator_nodes = CalculatorAgentNode(llm, system_message)
        self.create_graph()

    def create_graph(self):
        self.workflow.add_node(
            GET_FIRST_NUMBER_NODE, lambda state: self.calculator_nodes.get_first_number_node(state))
        self.workflow.add_node(
            GET_SECOND_NUMBER_NODE, lambda state: self.calculator_nodes.get_second_number_node(state))
        self.workflow.add_node(
            GET_RESULT_NODE, self.calculator_nodes.get_result_node)

        self.workflow.set_entry_point(GET_FIRST_NUMBER_NODE)

        self.workflow.add_edge(GET_FIRST_NUMBER_NODE, GET_SECOND_NUMBER_NODE)
        self.workflow.add_edge(GET_SECOND_NUMBER_NODE, GET_RESULT_NODE)
        self.workflow.add_edge(GET_RESULT_NODE, END)

    def compile_graph(self):
        return self.workflow.compile()
