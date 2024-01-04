""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Einführung in Markov-Entscheidungsprozesse", "Introduction to Markov Decision Processes") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Motivation
# - Markov Decision Processes (MDPs) are a mathematical framework for modeling decision making where outcomes are partly random and partly under the control of a decision maker.
# - They are used in many fields such as economics, game theory, control theory, operations research, artificial intelligence and robotics.

""" Code cell """
# %%
# An example code is shown which initializes a simple Markov Decision Process
states = ['s1', 's2', 's3']
actions = ['a1', 'a2', 'a3']
rewards = {'s1': {'a1': 5, 'a2': -1, 'a3': 0},
           's2': {'a1': -1, 'a2': 5, 'a3': 0},
           's3': {'a1': 0, 'a2': -1, 'a3': 5}}

""" Code cell """
# %%
# Another example code is shown where it determines the optimal action for a given state using a simple policy
def get_optimal_action(state):
    return max(rewards[state], key=rewards[state].get)
print(get_optimal_action('s1'))

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Definition
# - A Markov Decision Process is a tuple (S, A, P, R, γ) where:
#   - S is the state space.
#   - A is the action space.
#   - P is the probability transition function. P(s'|s,a) specifies the probability of arriving at state s' if action a is taken at state s.
#   - R is the reward function. R(s,a) gives the reward received after taking action a at state s.
#   - γ is the discount factor which determines the present value of future rewards.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Game Theory
# - In game theory, MDPs can be used to model and solve multiplayer games where each player has a strategy to maximize their score.
# - For example, in a board game, the state could be the current position of all pieces, the action could be the player's move, and the reward could be the score change due to that move.

""" Code cell """
# %%
# Here is a basic example of how one might set up an MDP for a simple game.
states = ['start', 'player1', 'player2', 'end']
actions = ['move1', 'move2', 'capture']
rewards = {'start': {'move1': 0, 'move2': 0, 'capture': 0},
           'player1': {'move1': 1, 'move2': -1, 'capture': 5},
           'player2': {'move1': -1, 'move2': 1, 'capture': -5},
           'end': {'move1': 0, 'move2': 0, 'capture': 0}}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Artificial Intelligence and Robotics
# - In artificial intelligence and robotics, MDPs can be used for planning under uncertainty.
# - For example, in robot navigation, the state could be the robot's position, the action could be the robot's motion commands, and the reward could be related to reaching the goal or avoiding obstacles.

""" Code cell """
# %%
# Here is a basic example of how one might set up an MDP for robot navigation.
states = ['s1', 's2', 's3', 's4']
actions = ['move_up', 'move_down', 'move_left', 'move_right']
rewards = {'s1': {'move_right': 1, 'move_up': -1, 'move_down': -1, 'move_left': -1},
           's2': {'move_right': -1, 'move_up': 1, 'move_down': -1, 'move_left': -1},
           's3': {'move_right': -1, 'move_up': -1, 'move_down': 1, 'move_left': -1},
           's4': {'move_right': -1, 'move_up': -1, 'move_down': -1, 'move_left': 1}}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Limitations
# - Although MDPs provide a robust framework for decision making under uncertainty, they have limitations. For instance, they assume that the decision maker has perfect knowledge of the state transition dynamics and rewards.
# - Also, in large state-action spaces, finding an optimal policy can be computationally intensive.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Hands-On Workshop
# In this workshop, we will create a simple MDP for a hypothetical scenario and implement an algorithm to find the optimal policy under this MDP. Stay tuned!

