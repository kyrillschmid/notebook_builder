""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Markov-Entscheidungsprozesse", "Markov Decision Processes") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Motivation
# - Markov Decision Processes (MDPs) form the theoretical basis for many areas of Machine Learning, particularly Reinforcement Learning.
# - Understanding MDPs paves the way to developing adaptive, intelligent systems that learn from their interactions with the environment.
# - With a solid understanding of MDPs, we can create algorithms that learn to perform tasks simply by trial and error, without explicit programming for each specific task.

""" Code cell """
# %%
# Code example demonstrating a simple Markov chain (not a decision process yet, but build up to it) 
import numpy as np

# Transition matrix for a simple weather model
# This is a Markov chain where the weather of each day is dependent only on the weather of the previous day
transition_matrix = np.array([[0.7, 0.3],  # Probabilities for ('sunny', 'rainy') given that yesterday was sunny
                              [0.3, 0.7]]) # Probabilities for ('sunny', 'rainy') given that yesterday was rainy
currentState = 'sunny'
markov_chain = [currentState]

np.random.seed(0)
for _ in range(10):
    if currentState == 'sunny':
        currentState = np.random.choice(['sunny', 'rainy'], p=transition_matrix[0])
    else:
        currentState = np.random.choice(['sunny', 'rainy'], p=transition_matrix[1])
    markov_chain.append(currentState)

print(f'Markov chain: {markov_chain}')

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Definition
# - A Markov Decision Process (MDP) is a 4-tuple (S, A, P, R) where:
# - S is a finite set of states.
# - A is a finite set of actions.
# - P is a state transition probability matrix.
# - R is a reward function.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Game playing
# - MDPs provide a strong theoretical foundation for designing artificial intelligence (AI) for games.
# - In a game, the state space could be the positions of all the pieces, the action space could be the set of all possible moves, and the reward could be associated with winning or losing the game.

""" Code cell """
# %%
# Code example demonstrating a simple Markov Decision Process in the context of a simple game
# In this game, the player starts at position 0, can either stay or move right, and gets a reward when reaching position 5
import pandas as pd

# State space
states = [0, 1, 2, 3, 4, 5]

# Action space
actions = ['stay', 'right']

# Transition probabilities and rewards
transition_probabilities = {action: pd.DataFrame(index=states, columns=states) for action in actions}

for state in states:
    if state < 5:
        transition_probabilities['stay'].loc[state,:] = [1 if state==s else 0 for s in states]
        transition_probabilities['right'].loc[state,:] = [1 if state+1==s else 0 for s in states]
    else:
        transition_probabilities['stay'].loc[state,:] = [1 if state==s else 0 for s in states]
        transition_probabilities['right'].loc[state,:] = [1 if state==s else 0 for s in states]
    
rewards = pd.Series([0, 0, 0, 0, 0, 1], index=states)

print(f'Transition probabilities for "stay":\n{transition_probabilities["stay"]}\n')
print(f'Transition probabilities for "right":\n{transition_probabilities["right"]}\n')
print(f'Rewards:\n{rewards}\n')

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Limitations
# - The Markov property assumes the future is independent of the past given the present. This might not hold in some real-world problems.
# - Large state and action spaces can make the problem computationally intractable.
# - Unknown transition probabilities and rewards may require learning from simulation or experience, which can be a complex problem in itself.

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Workshop
# - Now that you are familiar with Markov Decision Processes (MDPs), it's time to put your knowledge into practice!
# - Implement a MDP for a simple game and try to find an optimal policy using trial and error.
# - Use the example provided in this guide as a starting point. Make sure to revise and adapt the transition probabilities and rewards according to your specific game.

