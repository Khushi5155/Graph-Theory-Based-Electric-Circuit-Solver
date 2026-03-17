import streamlit as st
import os
from solver_placeholder.dummy_solver import get_dummy_solution

# Import your visualization function
from visualization.graph_visualizer import load_circuit, draw_circuit


st.set_page_config(page_title="Circuit Solver", layout="centered")

st.title("🔌 Graph-Based Circuit Solver")

st.write("Upload a circuit file or use the default sample circuit.")

# File uploader
uploaded_file = st.file_uploader("Upload Circuit File (.txt)", type=["txt"])


# If user uploads a file
if uploaded_file is not None:

    # Save uploaded file temporarily
    file_path = os.path.join("data", "uploaded_circuit.txt")

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

else:
    file_path = "data/sample_circuit.txt"
    st.info("Using default sample circuit.")


# Button to visualize
if st.button("Visualize Circuit"):

    try:
        edges, labels = load_circuit(file_path)

        st.write("### Circuit Graph Generated ")

        fig = draw_circuit(edges, labels)
        st.pyplot(fig)

        # Get dummy results
        node_voltages, branch_currents = get_dummy_solution(edges)

        # 🔹 Display Node Voltages
        st.subheader("Node Voltages")
        for node, voltage in node_voltages.items():
            st.write(f"V{node} = {voltage} V")

        # 🔹 Display Branch Currents
        st.subheader("Branch Currents")
        for branch, current in branch_currents.items():
            st.write(f"{branch} = {current} A")

        st.success("Visualization + Results complete!")

    except Exception as e:
        st.error(f"Error: {e}")