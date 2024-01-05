""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Markov Entscheidungsprozesse", "Markov Decision Processes") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Motivation
# - Markov Decision Processes (MDPs) serve as a mathematical framework for modeling decision making in situations where outcomes are partly random and partly under the control of a decision maker.
# - MDPs are useful for studying optimization problems solved via dynamic programming and reinforcement learning.

""" Code cell """
# %%
# The transition probabilities in a MDP are the equivalent of the kernel in a Markov chain
transition_probabilities = {
   's0': {'a0': {'s0': 0.5, 's2': 0.5},
          'a1': {'s2': 1}},
   's1': {'a0': {'s0': 0.7, 's1': 0.1, 's2': 0.2},
          'a1': {'s1': 0.95, 's2': 0.05}},
   's2': {'a0': {'s0': 0.4, 's2': 0.6},
          'a1': {'s0': 0.3, 's1': 0.3, 's2': 0.4}}
}

""" Code cell """
# %%
# Rewards for each state and action.
rewards = {
   's0': {'a0': {'s0': 0, 's2': 0},
          'a1': {'s2': 0}},
   's1': {'a0': {'s0': 0, 's1': -50, 's2': 40},
          'a1': {'s1': 0, 's2': -50}},
   's2': {'a0': {'s0': 0, 's2': 0},
          'a1': {'s0': 20, 's1': 20, 's2': -50}}
}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Formal Definition
# - A Markov Decision Process (MDP) is a tuple (S, A, P, R, γ) where:
#   - S is a finite set of states.
#   - A is a finite set of actions.
#   - P is a state transition probability matrix.
#   - R is a reward function. 
#   - γ is a discount factor γ ∈ [0, 1].

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Grid World
# - The Grid world is a popular application for MDP where an agent learns to reach the terminal from any cell on a grid.
# - The states are each cell in the grid, and the actions possible are moving in the four directions.

""" Code cell """
# %%
# Application example: Defining a simple grid world
grid_world = [
   ['#', ' ', ' ', ' ', ' ', ' ', ' ', 'T'],
   [' ', '#', ' ', '#', ' ', ' ', '#', ' '],
   [' ', ' ', ' ', ' ', ' ', ' ', '#', ' '],
   ['O', ' ', '#', ' ', ' ', ' ', ' ', ' '],
   [' ', ' ', ' ', ' ', '#', ' ', ' ', ' '],
   [' ', '#', ' ', ' ', ' ', ' ', ' ', ' '],
   [' ', '#', ' ', ' ', ' ', ' ', ' ', ' ']
]

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Robot Navigation
# - Robots use MDP to decide on the optimal path to reach a destination while avoiding obstacles.
# - Each state is the current location of the robot and the possible actions are the navigational directions.

""" Code cell """
# %%
# Application example: Defining a simple robot navigation task
robot_navigation = {
  "location": (1,1),
  "goal": (4,4),
  "obstacles": [(2,2), (3,3)],
  "actions": ["up", "down", "left", "right"]
}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Limitations 
# - MDPs make the key assumption of Markov property, which states that the future state only depends on the current state and not the history of states.
# - Determining the state-transition probabilities can be challenging in complex real-world scenarios.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Workshop: Building an MDP
# 1. Define the states: Identify the possible states of your system.
# 2. Define the actions: Identify the possible actions at each state.
# 3. Determine the state transition probabilities: Determine the chances of ending up in a next state given the current state and action.
# 4. Set the rewards: Determine the rewards for each action at each state, leading to each possible next state.
# 5. Select a discount factor: This determines the current value of future rewards.

