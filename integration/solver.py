import numpy as np

def solve_matrix(G, I):
    """
    Solve GV = I
    """
    try:
        V = np.linalg.solve(G, I)
        return V
    except Exception as e:
        print("Error solving matrix:", e)
        return None
    
def compute_node_voltages(V, node_mapping):
    node_voltages = {}

    for node, idx in node_mapping.items():
        node_voltages[node] = float(V[idx])

    # Ground node
    node_voltages[0] = 0.0

    return node_voltages
    