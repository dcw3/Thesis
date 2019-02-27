class TerminalSimulator:
    def __init__(self, terminal_mdp, agent):
        self.mdp = terminal_mdp
        self.agent = agent

    # return list of cumulative reward for each episode
    def simulate(self, n_episodes, initial_state):
        cum_rewards = [0] * n_episodes
        mdp = self.mdp
        self.agent.initialize(mdp.n_states, mdp.n_actions)
        for i in range(n_episodes):
            action = self.agent.begin_episode(initial_state, mdp.n_states, mdp.n_actions)
            current_state = initial_state
            current_time = 0
            while current_state not in mdp.terminal_states:
                current_time += 1
                reward, current_state = mdp.step(current_state, action, current_time)
                action = self.agent.step(reward, current_state, current_time)
                cum_rewards[i] += reward
            self.agent.end_episode()

        return cum_rewards