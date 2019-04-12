import numpy as np
import numbers


# i.i.d.
def dirichlet_transitions(alpha=1.0, n_states=1, n_actions=1):
    if isinstance(alpha, numbers.Real):
        alpha = np.array([alpha] * n_states)
    assert(len(alpha) == n_states)

    transition_matrices = [np.random.dirichlet(alpha, n_states) for _ in range(n_actions)]

    return transition_matrices


# TODO: allow n_dest_states to be a function rather than a constant
# n_dest_per_state is the number of states reachable in one step by each state
# n_dest_per_action is the number of states reachable in one step by each state-action pair
def simple_transitions(n_states=3, n_dest_per_action=None, n_dest_per_state=None, alpha=1.0, n_actions=1, terminal_states=None):
    if terminal_states is None:
        if n_states > 2:
            terminal_states = [n_states - 1, n_states - 2]

    if isinstance(n_dest_per_action, numbers.Real):
        n_dest_per_action = np.array([n_dest_per_action] * n_states)

    if isinstance(n_dest_per_state, numbers.Real):
        n_dest_per_state = np.array([n_dest_per_state] * n_states)

    if isinstance(alpha, numbers.Real):
        alpha_arr = np.array([alpha] * n_states)
    else:
        alpha_arr = alpha

    transition_matrices = [np.zeros((n_states, n_states)) for _ in range(n_actions)]
    non_terminal_states = set(range(n_states)) - set(terminal_states)
    for s in non_terminal_states:
        reachable_states = np.random.choice(n_states, size=n_dest_per_state[s], replace=False)
        for a in range(n_actions):
            dest_states = np.random.choice(reachable_states, size=n_dest_per_action[s], replace=False)
            alph_array = np.array([alpha_arr[s]] * n_dest_per_action[s])
            dest_probs = np.random.dirichlet(alph_array, 1)[0]
            all_probs = np.zeros(n_states)
            for i in range(n_dest_per_action[s]):
                all_probs[dest_states[i]] = dest_probs[i]
            transition_matrices[a][s] = all_probs

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
