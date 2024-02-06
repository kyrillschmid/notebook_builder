# j2 from 'macros.j2' import header
# {{ header("DQN", "DQN") }}

# %% [markdown] lang="en" tags=["slide"]
# ## Introduction to DQN
# - DQN stands for Deep Q-Network, a key algorithm in Reinforcement Learning
# - It combines classical Q-Learning with deep neural networks
# - This tutorial will guide you through implementing DQN with PyTorch

# %% [markdown] lang="en" tags=["slide"]
# ## Initial Setup
# - Import necessary libraries including gym, collections, and random for environment and data handling
# - Import PyTorch related libraries for building the neural network and optimization

# %%
import gym
import collections
import random

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# %% [markdown] lang="en" tags=["slide"]
# ## Setting Hyperparameters
# - Hyperparameters are crucial for training deep learning models
# - We set learning rate, gamma (discount factor), buffer limit, and batch size
# - These values can be adjusted based on the problem and environment

# %%
#Hyperparameters
learning_rate = 0.0005
gamma         = 0.98
buffer_limit  = 50000
batch_size    = 32
# %% [markdown] lang="en" tags=["slide"]
# ## Introduction to DQN
# - Deep Q-Networks (DQN) are a breakthrough in reinforcement learning that combine Q-Learning with deep neural networks
# - This session covers the implementation of a DQN agent
# - We will explore key components such as the replay buffer

# %% [markdown] lang="en" tags=["slide"]
# ## The Replay Buffer
# - The Replay Buffer is crucial for stabilizing the learning process in DQN
# - It stores transitions that the agent experiences
# - This allows the agent to sample from this buffer to break correlation between consecutive learning samples

# %%
import collections
import random
import torch

# %% [markdown] lang="en" tags=["slide"]
# ## Initializing the Replay Buffer
# - The buffer is initialized with a maximum limit
# - It uses a deque, a double-ended queue perfect for this FIFO structure

# %%
class ReplayBuffer():
    def __init__(self, buffer_limit=50000):
        self.buffer = collections.deque(maxlen=buffer_limit)

# %% [markdown] lang="en" tags=["slide"]
# ## Storing Transitions
# - Transitions, consisting of state, action, reward, next state, and done flag, are stored in the buffer
# - This makes the replay buffer grow with each experience until it hits its limit

# %%
    def put(self, transition):
        self.buffer.append(transition)

# %% [markdown] lang="en" tags=["slide"]
# ## Sampling from the Buffer
# - The buffer randomly samples a mini-batch of transitions
# - This is used to train the neural network with a more stable data set
# - The sampled transitions are separated into tensors for each component

# %%
    def sample(self, n):
        mini_batch = random.sample(self.buffer, n)
        s_lst, a_lst, r_lst, s_prime_lst, done_mask_lst = [], [], [], [], []

        for transition in mini_batch:
            s, a, r, s_prime, done_mask = transition
            s_lst.append(s)
            a_lst.append([a])
            r_lst.append([r])
            s_prime_lst.append(s_prime)
            done_mask_lst.append([done_mask])

        return torch.tensor(s_lst, dtype=torch.float), torch.tensor(a_lst), \
               torch.tensor(r_lst), torch.tensor(s_prime_lst, dtype=torch.float), \
               torch.tensor(done_mask_lst)

# %% [markdown] lang="en" tags=["slide"]
# ## Buffer Size
# - Knowing the current size of the buffer is useful for various reasons
# - It gives insight into how much data is available for training the network

# %%
    def size(self):
        return len(self.buffer)
# %% [markdown] lang="en" tags=["slide"]
# ## Introduction to DQN
# - DQN stands for Deep Q-Network, which integrates neural networks with Q-learning
# - It allows agents to take actions in environments with high-dimensional observation spaces
# - We will build a simple DQN model using PyTorch

# %% [markdown] lang="en" tags=["slide"]
# ## Defining the Q-Network
# - The Q-Network estimates the value of taking each action in a given state
# - It's a neural network with input dimension equal to the state dimension, and output dimension equal to the number of actions
# - Our example Q-Network has 3 fully connected layers

# %%
import torch
import torch.nn as nn
import torch.nn.functional as F
import random

class Qnet(nn.Module):
    def __init__(self):
        super(Qnet, self).__init__()
        self.fc1 = nn.Linear(4, 128)  # First Fully Connected Layer
        self.fc2 = nn.Linear(128, 128)  # Second Fully Connected Layer
        self.fc3 = nn.Linear(128, 2)  # Output Layer

    def forward(self, x):
        x = F.relu(self.fc1(x))  # Activation function for first layer
        x = F.relu(self.fc2(x))  # Activation function for second layer
        x = self.fc3(x)  # No activation, direct mapping to output
        return x

# %% [markdown] lang="en" tags=["slide"]
# ## Action Selection Strategy
# - DQN uses an $\epsilon$-greedy strategy for action selection
# - Random actions are taken with probability $\epsilon$ to encourage exploration
# - Otherwise, the action with the highest Q-value is chosen for exploitation

# %%
def sample_action(self, obs, epsilon):
    out = self.forward(obs)
    coin = random.random()
    if coin < epsilon:
        return random.randint(0,1)  # Random action
    else : 
        return out.argmax().item()  # Action with the highest Q-value

# Adding the sample_action method to our Qnet class
Qnet.sample_action = sample_action

# %% [markdown] lang="en" tags=["slide"]
# ## Summary
# - We designed a simple Q-Network architecture for DQN
# - We integrated an $\epsilon$-greedy action selection method
# - This foundation enables us to implement a full DQN agent for complex environments
# %% [markdown] lang="en" tags=["slide"]
# ## Introduction to DQN Training
# - Discuss how a DQN (Deep Q-Network) learns from interactions with the environment
# - Describe the structure of the `train` function for a DQN agent
# - Explain the importance of using a target network in stabilizing DQN training

# %% [markdown] lang="en" tags=["slide"]
# ## Sampling Experience from Memory
# - Understanding how experiences are sampled from memory
# - Explanation of the components of an experience tuple: state, action, reward, next state, and done mask
# - The role of a batch size in sampling experiences for training

# %%
def train(q, q_target, memory, optimizer):
    for i in range(10):
        s, a, r, s_prime, done_mask = memory.sample(batch_size)

# %% [markdown] lang="en" tags=["slide"]
# ## Calculating Q-Values
# - Utilize the current Q-network to calculate the Q-values for the sampled states
# - Selecting the Q-value corresponding to the taken action
# - Calculating the maximum Q-value for the next state from the target Q-network

# %%
        q_out = q(s)
        q_a = q_out.gather(1, a)
        max_q_prime = q_target(s_prime).max(1)[0].unsqueeze(1)

# %% [markdown] lang="en" tags=["slide"]
# ## Target Q-Value Calculation
# - Importance of calculating target Q-values for training stability
# - Utilizing rewards, gamma (discount factor), and the done mask for calculating target Q-values
# - How the done mask helps in handling terminal states

# %%
        target = r + gamma * max_q_prime * done_mask

# %% [markdown] lang="en" tags=["slide"]
# ## Loss Calculation and Optimization
# - Calculating the loss using Smooth L1 Loss between the predicted Q-values and the target Q-values
# - Importance of zeroing the gradients before backward propagation
# - Performing a single optimization step to update the Q-network's weights

# %%
        loss = F.smooth_l1_loss(q_a, target)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
# %% [markdown] lang="en" tags=["slide"]
# ## Introduction to DQN (Deep Q-Network)
# - Deep Q-Networks combine Q-Learning with deep neural networks to allow RL to work with high-dimensional state spaces.
# - This technique was popularized by DeepMind in learning to play Atari games directly from pixels.
# - Here, we build a basic DQN to tackle the CartPole environment from OpenAI Gyms.

# %% [markdown] lang="en" tags=["slide"]
# ## Setting up the Environment and Neural Network
# - Initialize the CartPole environment, which is a balanced pole task.
# - Define the Q-network architecture to approximate Q-values.
# - Set up a target Q-network which helps in stabilizing learning.

# %%
import gym
import torch
import torch.nn as nn
import torch.optim as optim

# %%
class Qnet(nn.Module):
    def __init__(self):
        super(Qnet, self).__init__()
        # Neural network layers here
    
    def forward(self, x):
        # Forward pass through the network
        return x

    def sample_action(self, obs, epsilon):
        # Epsilon-greedy action sampling
        return action

# %%
env = gym.make('CartPole-v1')
q = Qnet()
q_target = Qnet()
q_target.load_state_dict(q.state_dict())
learning_rate = 0.0004

# %% [markdown] lang="en" tags=["slide"]
# ## Experience Replay
# - Implement Replay Buffer to store and sample experiences.
# - Experience replay decouples the experience samples and reduces the variance in updates.

# %%
class ReplayBuffer:
    def __init__(self):
        # Initialization code
    
    def put(self, transition):
        # Store transitions in the buffer
    
    def sample(self, n):
        # Sample a batch of transitions
    
    def size(self):
        # Return the current size of the buffer

memory = ReplayBuffer()

# %% [markdown] lang="en" tags=["slide"]
# ## Training Loop
# - Iterate over episodes, sampling actions and storing experiences.
# - Periodically update the Q-network by sampling batches from the Replay Buffer.
# - Use target Q-network to stabilize the training.

# %%
optimizer = optim.Adam(q.parameters(), lr=learning_rate)
print_interval = 20
score = 0.0  

for n_epi in range(10000):
    epsilon = max(0.01, 0.08 - 0.01*(n_epi/200))  # Linear annealing from 8% to 1%
    s, _ = env.reset()
    done = False

    while not done:
        a = q.sample_action(torch.from_numpy(s).float(), epsilon)      
        s_prime, r, done, truncated, info = env.step(a)
        done_mask = 0.0 if done else 1.0
        memory.put((s,a,r/100.0,s_prime, done_mask))
        s = s_prime

        score += r
        if done:
            break
            
    if memory.size()>2000:
        train(q, q_target, memory, optimizer)

    if n_epi%print_interval==0 and n_epi!=0:
        q_target.load_state_dict(q.state_dict())
        print("n_episode :{}, score : {:.1f}, n_buffer : {}, eps : {:.1f}%".format(
                                                        n_epi, score/print_interval, memory.size(), epsilon*100))
        score = 0.0
env.close()

# %% [markdown] lang="en" tags=["slide"]
# ## Conclusion and Observations
# - We implemented a basic DQN agent for the CartPole environment.
# - Key components include the Q-network, target Q-network, and experience replay.
# - Observing the agent's performance and tuning parameters like epsilon decay is crucial for improving performance.
