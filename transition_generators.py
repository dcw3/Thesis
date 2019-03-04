import numpy as np
import numbers

# i.i.d.
def dirichlet_transitions(alpha=1.0, n_states=1, n_actions=1):
    if isinstance(alpha, numbers.Real):
        alpha_arr = np.array([alpha] * n_states)
    else:
        alpha_arr = alpha
    assert(len(alpha_arr) == n_states)

    transition_matrices = [np.random.dirichlet(alpha_arr, n_states) for _ in range(n_actions)]

    return transition_matrices

import networkx as nx
from networkx.drawing.nx_agraph import write_dot

def write_to_dot(transition_matrix, path='mc.dot', cutoff=0, terminal_states=[]):
    G = nx.DiGraph()
    edge_labels = {}
    n_states = len(transition_matrix[0])

    for i in range(n_states):
        for j in range(n_states):
            rate = transition_matrix[i][j]
            if rate > cutoff and i not in terminal_states:
                G.add_edge(i, j, weight=rate, label="{:.02f}".format(rate))
                edge_labels[(i, j)] = "{:.02f}".format(rate)

    write_dot(G, path)