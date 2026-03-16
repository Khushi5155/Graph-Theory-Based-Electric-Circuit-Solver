# Graph-Theory-Based Electric Circuit Solver

## Project Overview

This project implements an **Electric Circuit Solver using Graph Theory** concepts.  
The circuit is modeled as a **graph**, where:

- **Nodes (Vertices)** represent circuit nodes

- **Branches (Edges)** represent circuit elements such as resistors and voltage sources

The solver will analyze the circuit using **Kirchhoff's Laws and matrix methods** to compute node voltages and branch currents.

This project is developed as a **Project Based Learning (PBL)** task for the **Circuits and Systems course**.

---

## Objectives

- Represent electrical circuits using **graph theory**

- Automatically generate **graph structures from circuit inputs**

- Apply **Kirchhoff Current Law (KCL)** and **Kirchhoff Voltage Law (KVL)**

- Solve circuits using **matrix-based numerical methods**

- Provide **visual representation of circuits and results**

---

## Project Architecture

```
Circuit Input
     ↓
Graph Builder
     ↓
Matrix Generator
     ↓
Numerical Solver
     ↓
Visualization & UI
```

---

## Project Folder Structure

```
Graph_Circuit_Solver
│
├── main.py
│
├── data
│   └── sample_circuit.txt
│
├── ui
│   └── interface.py
│
├── visualization
│   └── graph_visualizer.py
│
├── results
│   └── result_display.py
│
├── integration
│   └── api.py
│
├── solver_placeholder
│   └── dummy_solver.py
│
└── README.md
```

---

## Input Format

Circuit elements are defined in a simple text format:

```
Component Node1 Node2 Value
```

Example:

```
R1 1 2 10
R2 2 3 5
R3 3 0 20
V1 1 0 12
```

Meaning:

| Component | Node1 | Node2 | Value |
| --------- | ----- | ----- | ----- |
| R1        | 1     | 2     | 10Ω   |
| R2        | 2     | 3     | 5Ω    |
| R3        | 3     | 0     | 20Ω   |
| V1        | 1     | 0     | 12V   |

---

## Technologies Used

- **Python**

- **NetworkX** – graph modeling

- **Matplotlib** – graph visualization

- **Streamlit / Tkinter** – user interface

- **NumPy** – matrix computations

---

## Team Responsibilities

### Aayush Kumar Jha – Graph Modeling

- Convert circuit components into graph structures

- Generate incidence matrices

### Sunidhi Singh – Matrix Formulation

- Implement KCL and KVL equations

- Generate conductance matrices

### Khushi Kumari – Numerical Solver

- Solve circuit equations using Python (NumPy)

### Pratyush – Visualization & UI

- Build the user interface

- Visualize circuit graphs

- Display node voltages and branch currents

- Integrate outputs from other modules

---

## Expected Output

The system should provide:

1. Graph representation of the circuit

2. Node voltages

3. Branch currents

4. Visualization of circuit topology

Example output:

```
Node Voltages
V1 = 12V
V2 = 7.5V
V3 = 0V

Branch Currents
I_R1 = 0.45A
I_R2 = 0.20A
```

---

## Future Improvements

- Support for more components (capacitors, inductors)

- AC circuit analysis

- Interactive circuit editor

- Advanced simulation features
