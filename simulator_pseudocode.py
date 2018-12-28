# utility function
def matrix_factory(arguments):
	pass

# assume finite state, action space
class MDP:
	def __init__(transition_matrices, reward_functions, initial_state):
		# verify transition_matrices, reward_functions
			# len(transition_matrices) = # of actions
        	# transition_matrices[i] = transition matrix corresponding to action i
        	# len(transition_matrices[0][0]) = len(reward_functions) = number of states
		
		self.current_state = initial_state
		self.initial_reward = reward_functions[initial_state](0)

	def step(action, time):
		# update current_state based on action

		reward = reward_functions[current_state](time)
		
		return reward, current_state

class Agent:
	# should I allow user to specify priors?
	def __init__(initial_state, num_states, num_actions):
	    pass
		
	# do I need to specify previous_state and action? Or should I expect the Agent to keep track of that itself?
	def step(reward, current_state, time):
	    # different for each Agent
		return action

def test(agent, mdp, total_time):
	all_rewards = []
	action = agent.step(mdp.initial_reward, mdp.current_state, 0)
	for t in range(total_time):
		reward, next_state = mdp.step(action, t)
		all_rewards.append(reward)
		action = agent.step(reward, next_state, t)
	return all_rewards