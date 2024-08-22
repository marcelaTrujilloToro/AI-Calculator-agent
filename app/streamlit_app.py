import streamlit as st
from main import calculator_graph, initial_state  

st.title("Calculator with LangChain & OpenAI")

# Función para regenerar números
def regenerate_numbers():
    st.session_state.state = initial_state.copy()
    st.session_state.state = calculator_graph.calculator_nodes.get_first_number_node(st.session_state.state)
    st.write(f"First number: {st.session_state.state['first_number']}")
    st.session_state.state = calculator_graph.calculator_nodes.get_second_number_node(st.session_state.state)
    st.write(f"Second number: {st.session_state.state['second_number']}")

# Inicializa el estado en `st.session_state` si no existe o si se presiona "Restaurar"
if "state" not in st.session_state:
    regenerate_numbers()

if st.button("Reset"):
    regenerate_numbers()

# Selector de operación
operation = st.selectbox(
    "Select operation:",
    ("Addition",
    "Subtraction",
    "Multiplication",
    "Division"
    )
)

# Mapea la operación seleccionada a los valores correspondientes
operation_map = {
    "Addition": "1",
    "Subtraction": "2",
    "Multiplication": "3",
    "Division": "4"
}

selected_operation = operation_map[operation]

# Botón para calcular el resultado
if st.button("Calculate"):
    # Actualiza la operación seleccionada en el estado
    st.session_state.state["operation"] = selected_operation

    # Calcula el resultado usando el estado persistente
    result_state = calculator_graph.calculator_nodes.get_result_node(st.session_state.state)
    st.write(f"The result is {result_state['result']}")