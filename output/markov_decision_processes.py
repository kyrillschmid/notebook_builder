""" Header cell """
# j2 from 'macros.j2' import header
# {{ header("Markov-Entscheidungsprozesse (MDP)", "Markov Decision Processes (MDP)") }}

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Motivation
# - Decision-making is central to many AI systems. Most of these systems make crucial decisions under uncertain conditions, therefore they must take into account both the current situation and future consequences.
# - Markov Decision Processes (MDPs) provides a mathematical framework to model decision making in situations where outcomes are partly random and partly under the control of a decision maker.

""" Code cell """
# %%
# Sample code showing a simple Markov Decision Process.
class MDP:
  def __init__(self, initialState, actionSpace, transitionProbabilities, rewards, discountFactor):
    self.state = initialState
    self.actionSpace = actionSpace
    self.tp = transitionProbabilities  # e.g., {s: {a: {s': (prob, reward), ...}, ...}, ...}
    self.r = rewards  # e.g., {s: {a: {s': r, ...}, ...}, ...}
    self.df = discountFactor  # [0, 1]

  def transition(self, action):
    outcomes = self.tp[self.state][action]
    nextState = np.random.choice(list(outcomes.keys()), p=list(outcomes.values()))
    reward = self.r[self.state][action][nextState]
    self.state = nextState
    return nextState, reward

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Markov Decision Processes (MDPs): Formal Definition
# - An MDP is defined by a tuple $(S, A, P^a, R^a, γ)$ where:
#  - $S$ is a set of states,
#  - $A$ is a set of actions,
#  - $P^a_{ss'} = P[S_{t+1}=s' | S_t=s, A_t=a]$ is the probability that action $a$ in state $s$ at time $t$ will lead to state $s'$ at time $t+1$.
#  - $R^a_{ss'} = R[S_{t+1}=s', S_t=s, A_t=a]$ is the expected immediate reward after transitioning from state $s$ to state $s'$, due to action $a$,
#  - γ is a discount factor γ ∈ [0, 1].

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Reinforcement Learning
# - MDPs are a core part of many reinforcement learning algorithms, providing a framework for understanding the dynamics of learning to make optimal decisions over time.
# - Key approaches in reinforcement learning like Q-learning, SARSA and Policy Iteration can be understood in terms of MDPs.

""" Code cell """
# %%
# Sample code showing how MDPs enable reinforcement learning. This example uses Q-learning.
import numpy as np

class QLearning:
  def __init__(self, actionSpace, learningRate, discountFactor, explorationRate):
    self.qTable = {}
    self.aSpace = actionSpace
    self.lr = learningRate
    self.df = discountFactor
    self.er = explorationRate

  def chooseAction(self, state):
    # Exploration vs exploitation
    if np.random.uniform(0, 1) < self.er:
      # Explore: choose a random action
      action = np.random.choice(self.aSpace)
    else:
      # Exploit: choose the action with highest q-value (expected future reward)
      actionValues = [self.getQ(state, a) for a in self.aSpace]
      action = self.aSpace[np.argmax(actionValues)]
    return action

  def getQ(self, state, action):
    return self.qTable.get((state, action), 0)

  def learn(self, state, action, reward, nextState):
    oldQ = self.getQ(state, action)
    newQ = reward + self.df * max([self.getQ(nextState, a) for a in self.aSpace])
    self.qTable[(state, action)] = oldQ + self.lr * (newQ - oldQ)

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Application: Robotics
# - In robotics, MDPs can be used to continuously take the best action based on the robot's current state and surroundings.
# - This allows the robot to make decisions in real-time and adapt to changing conditions.

""" Code cell """
# %%
# Sample code
class RobotMDP(MDP):
  def __init__(self, initialState, actionSpace, transitionProbabilities, rewards, discountFactor):
    super().__init__(initialState, actionSpace, transitionProbabilities, rewards, discountFactor)

""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Limitations of MDPs
# - One of the main limitations of MDPs is the assumption of Markov property, which says the future states depend only on the current state and action, not on the sequence of events that preceded it. In many real-world scenarios, this assumption is not valid.
# - MDPs can suffer from the "curse of dimensionality" - an exponential growth in computation time with the increase in the number of states or actions.
  
""" Slide cell """
# %% [markdown] lang="en" tags=["slide"]
# ## Workshop: Building Your Own MDP
# - Given a specific scenario, how would you construct an MDP to model it?
# - What are the states, actions, and rewards in this scenario?
# - How do you define the transition probabilities between states for different actions?
# In this workshop, we guide you through the whole process by taking a simple example. Let's construct an MDP for a simple robotic cleaner. The state could be the current location of the robot, actions could be the possible movements of the robot, and rewards could be associated with the cleanliness of the area. Future lessons of this course will guide you on how to solve this MDP using various Reinforcement Learning techniques like Q-learning, SARSA etc.

