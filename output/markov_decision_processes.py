""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Markov-Entscheidungsprozesse", "Markov Decision Processes") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Motivation
# - Markov decision processes (MDPs) provide a mathematical framework for modeling sequential decision-making scenarios, and are a key element in reinforcement learning.
# - Understanding MDPs allows us to model complex environments and learning systems, and is a prerequisite for studying and applying reinforcement learning algorithms.

""" Code cell """
# %%
# A simple implementation of an MDP
states = ('Rain', 'Nice')
actions = ('Walk', 'Shop', 'Clean')
rewards = {(('Rain', 'Walk'), ('Rain')): -1, (('Rain', 'Shop'), ('Nice')): 2, (('Nice', 'Walk'), ('Rain')): 3}

def transition(s, a):
    # Put your transition logic here
    pass

def reward(s, a, s_prime):
    return rewards.get((s,a), s_prime, 0)

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Definition
# - A Markov Decision Process (MDP) is defined by a tuple (S, A, P, R, γ), where:
#   - S is a set of states
#   - A is a set of actions
#   - P is a state transition function, P(s'|s,a) is the probability of ending in state s' given the current state s and action a
#   - R is a reward function, R(s,a,s') is the reward received after transitioning from state s to state s' due to action a
#   - γ is the discount factor, which determines the present value of future rewards

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Control of a robotic system
# - A robotic system's behaviour can be modelled as an MDP. The states represent the positions and velocity of the robot, the actions represent the control commands, and the rewards could be set to encourage reaching a target and avoiding obstacles.

""" Code cell """
# %%
# Assume there exist functions to get current state and perform action
# These functions are usually provided by the robot control system or simulator
def get_current_state():
    pass

def perform_action(action):
    pass

# The MDP based control algorithm
state = get_current_state()
action = None  # Choose an action based on your current understanding of the environment and the MDP model
perform_action(action)


""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Game playing strategy
# - The process of playing a game can be modelled as an MDP. The states will represent the current board configuration, the actions are the legal moves, and the rewards can be set to encourage winning the game and penalize losing.
 
""" Code cell """
# %%
# Assume there exists functions to get current board configuration, get legal moves, make a move and get the game result
# These functions are usually provided by the game engine or library

def get_current_board():
    pass

def get_legal_moves():
    pass

def make_move(move):
    pass

def get_game_result():
    pass

# The MDP based game playing algorithm
board = get_current_board()
moves = get_legal_moves()
move = None  # Choose a move based on your current understanding of the game and the MDP model
make_move(move)


""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Limitations
# - MDPs assume that the decision maker has full knowledge of the state transition probabilities and reward functions, which may not be the case in many real-world scenarios.
# - Large state or action spaces can make solving MDPs computationally infeasible.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Workshop: Practice with Markov Decision Processes
# - Workshop attendees will be given access to a Python environment with the necessary libraries and functions to implement and solve MDPs.
# - Hands-on tasks will include defining and solving MDP problems, and implementing reinforcement learning algorithms based on MDPs.

