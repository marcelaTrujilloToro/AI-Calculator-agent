from langchain_core.messages import HumanMessage
from utils.operations import sum_numbers, substract_numbers, multiply_numbers, divide_numbers


def get_first_number_node(state, llm, system_message):
    human_message = HumanMessage(
        content="Generate a random number between 1 and 10 and return it only as a number, without additional text.")
    messages = [system_message, human_message]
    ia_response = llm.invoke(messages)
    response = int(ia_response.content)
    state["first_number"] = response
    print(f"First number: {state["first_number"]}")
    return state


def get_second_number_node(state,  llm, system_message):
    human_message = HumanMessage(
        content="Generate a random number between 1 and 10 and return it only as a number, without additional text.")
    messages = [system_message, human_message]
    ia_response = llm.invoke(messages)
    response = int(ia_response.content)
    state["second_number"] = response
    print(f"Second number: {state["second_number"]}")
    return state


def get_result_node(state):
    first_number = state["first_number"]
    second_number = state["second_number"]

    operation = input(
        "Which operation would you like to perform? (1: addition, 2: subtraction, 3: multiplication, 4: division)")

    operation_map = {
        "1": ("addition", sum_numbers),
        "2": ("subtraction", substract_numbers),
        "3": ("multiplication", multiply_numbers),
        "4": ("division", divide_numbers)
    }

    operation_selected = operation_map.get(operation)

    if operation_selected is None:
        print("Invalid operation")
        return state

    operation_name, operation_func = operation_selected
    result = operation_func(first_number, second_number)

    state["result"] = result
    print(
        f"The result of the {operation_name} between {first_number} and {second_number} is: {result}")
    return state
