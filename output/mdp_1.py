""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Markov Entscheidungsprozesse", "Markov Decision Processes") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Motivation
# - Markov Decision Processes (MDPs) are the mathematical foundation of many reinforcement learning algorithms
# - It provides a way of modeling sequential decision-making situations
# - It's the key to understanding different environments and implementing intelligent algorithms that can perform well in such environments

""" Code cell """
# %%
import numpy as np
# Define states and actions

states = ["sleep", "icecream", "run"]
actions = ["sleep", "icecream", "run"]

# Initialize transition probabilities

P = {}
for s in states:
  P[s] = {}
  for a in actions:
    P[s][a] = {s2: 0 for s2 in states}
    
# For each action, define transition probabilities for new states

P["sleep"]["sleep"]["sleep"] = 1
P["sleep"]["icecream"]["icecream"] = 1
P["sleep"]["run"]["run"] = 0.7
P["sleep"]["run"]["sleep"] = 1 - 0.7

# This is a basic set up for an MDP

""" Code cell """
# %%
# Reward structure

R = {
    "sleep": {"sleep": 0, "icecream": 0, "run": -1},  
    "icecream": {"sleep": 0, "icecream": 1, "run": 1}, 
    "run": {"sleep": 0, "icecream": 1, "run": 2},  
}
    
# This will define the reward the agent will get for each action in each state. 

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Formal Definition
# A Markov decision process (MDP) is defined by a tuple $(S, A, P, R, \gamma)$, where:
# - $S$ is a finite set of states
# - $A$ is a finite set of actions
# - $P$ is a state transition probability matrix, $P_{ss'}^a = \text{Prob}(S_{t+1}=s'|S_t=s, A_t=a)$
# - $R$ is a reward function, $R_s^a = E[R_{t+1}|S_t=s, A_t=a]$
# - and $\gamma$ is a discount factor, $\gamma \in [0, 1]$

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Game Playing
# - Markov decision processes can be used to create game-playing AI.
# - Each state in the game (like Chess) is represented as a state in the MDP.
# - The action of moving a piece leads to a new state.

""" Code cell """
# %%
# A simplified abstract representation of a game-playing AI using MDP

class GameState:
    def __init__(self):
        self.to_move = 'A'
        self.utility = 0
        self.board = None
        self.moves = None 

class Game:
    def actions(self, state):
        "current player legal moves"
    def result(self, state, move):
        "new game state from a move"
    def utility(self, state, player):
        "player's score"
    def terminal_test(self, state):
        "game over?"
    def to_move(self, state):
        "current player"

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Robot Navigation
# - In a real world scenario, consider a room-cleaning robot.
# - The state of the room (Clean/Dirty) and robot's position can be represented as states in the MDP.
# - The actions could be 'Clean', 'Move to another position' etc.

""" Code cell """
# %%
class State:
    def __init__(self):
        self.room_condition = ['Dirty', 'Clean']
        self.robot_position = None 

class Robot:
    def perform_action(self, state, action):
        if action == 'Clean':
            state.room_condition = 'Clean'
        elif action == 'Move':
            state.robot_position = 'another_position'
             
    def get_reward(self, state):
        if state.room_condition == 'Clean':
            return 1
        else:
            return -1

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Limitations
# - Limited to problems that have the Markov property (next state only depends on current state, not on previous states)
# - For many practical problems, state space can be enormous, leading to computational challenges
# - In some cases, exact values for transition probabilities or rewards are not available, in which case we need to make approximations.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Hands-On Workshop: Implement a Tic-Tac-Toe AI
# - Define the game rules
# - Translate the game into a MDP
# - Implement a reinforcement learning algorithm to play the game

