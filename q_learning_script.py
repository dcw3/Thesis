import mdp
import q_learning_agent
import simulator
import transition_generators
import numpy as np
import time

np.random.seed(15)

trans = transition_generators.dirichlet_transitions(1, 10, 3)
transition_generators.write_to_dot(trans[0], path='mc0.dot', cutoff=0.1, terminal_states=[8, 9])
transition_generators.write_to_dot(trans[1], path='mc1.dot', cutoff=0.1, terminal_states=[8, 9])
transition_generators.write_to_dot(trans[2], path='mc2.dot', cutoff=0.1, terminal_states=[8, 9])

reward_funcs = [lambda _: 0, lambda _: 0, lambda _: 0, lambda _: 0, lambda _: 0, lambda _: 0, lambda _: 0, lambda _: 0, lambda _: 0, lambda _: 1]
# reward_funcs = [lambda _: 0, lambda _: 0, lambda _: 1]

m = mdp.TerminalMDP(trans, reward_funcs, terminal_states=[8, 9])
ag = q_learning_agent.QLearningAgent(mdp=m, discount_rate=0.9, lambda_val=0.5, learning_rate=0.1)

sim = simulator.TerminalSimulator(m, ag)
begin_time = time.time()
cum_rewards = sim.simulate(100000, 0)
print('Seconds to run: ', np.round(time.time() - begin_time, decimals=1))
# print(cum_rewards)
a = cum_rewards[0:100]
print(a)
print(np.mean(a))
b = cum_rewards[-100:]
print(b)
print(np.mean(b))

print(np.round(ag.q_vals, decimals=2))