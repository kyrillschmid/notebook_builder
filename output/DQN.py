# j2 from 'macros.j2' import header
# {{ header("DQN", "DQN") }}

# %% [markdown] lang="en" tags=["slide"]
# ## Introduction to Reinforcement Learning
# - Reinforcement Learning (RL) is a branch of machine learning where agents learn to make decisions
# - It involves agents interacting with an environment to achieve a goal
# - Deep Q-Networks (DQN) are a popular and effective technique in RL

# %% [markdown] lang="en" tags=["slide"]
# ## Setting up the Environment
# - We'll be using the OpenAI Gym environment for our DQN example
# - Gym provides various environments to test and train RL algorithms
# - It's a critical tool for prototyping and validating AI systems

# %%
import gym
import collections
import random

# %% [markdown] lang="en" tags=["slide"]
# ## Implementing the DQN Agent
# - First, import necessary libraries for neural network implementation and optimization
# - `torch` and its modules will be used for creating and training the neural network

# %%
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

# %% [markdown] lang="en" tags=["slide"]
# ## Neural Network for Q-Value Prediction
# - The brain of our DQN Agent is a neural network that predicts Q-Values
# - Q-Values represent the "quality" or value of taking an action in a given state
# - Our network will be a simple feedforward neural network

# %% [markdown] lang="en" tags=["slide"]
# ## Summary
# - In this section, we laid the groundwork for creating a DQN Agent
# - We introduced the Gym environment and necessary PyTorch tools
# - The next steps include designing the neural network architecture and training the DQN Agent
# %% [markdown] lang="en" tags=["slide"]
# ## Hyperparameters in DQN
# - Hyperparameters are crucial in Reinforcement Learning as they directly influence the performance of the model.
# - In this section, we will discuss why we choose specific values for our DQN model's hyperparameters.
# - Understanding these will aid in fine-tuning for different tasks and environments.

# %% 
learning_rate = 0.0005
gamma         = 0.98
buffer_limit  = 50000
batch_size    = 32

# %% [markdown] lang="en" tags=["slide"]
# ## Understanding Learning Rate
# - The learning rate determines how much we adjust the weights of our network with respect the loss gradient.
# - A smaller value like 0.0005 ensures that we make smaller updates, preventing overshooting minimum.
# - This value might need adjustments based on the specific characteristics of the environment.

# %% [markdown] lang="en" tags=["slide"]
# ## The Role of Gamma (Discount Factor)
# - Gamma (γ) determines the importance we give to future rewards. A high value approximates to considering long-term gains.
# - Here, we use 0.98 to indicate that future rewards are very important but slightly less than immediate rewards.
# - Adjusting gamma involves balancing between short-term and long-term benefits.

# %% [markdown] lang="en" tags=["slide"]
# ## Buffer Limit and Experience Replay
# - The buffer limit sets the size of the replay buffer, where we store experiences to sample from later.
# - A large buffer, like 50000, allows the agent to learn from a wide range of past experiences, improving generalization.
# - This parameter needs to be large enough to contain a diverse set of experiences but balanced to avoid immense memory usage.

# %% [markdown] lang="en" tags=["slide"]
# ## Batch Size for Learning
# - Batch size determines how many experiences we sample from the buffer to update the network at a time.
# - Using a moderate size like 32 helps in stabilizing the learning process.
# - It balances computational efficiency with the benefit of learning from multiple experiences simultaneously.
# %% [markdown] lang="en" tags=["slide"]
# ## Introduction to Replay Buffers in DQN
# - Replay Buffers are an essential component in Deep Q-Networks (DQN), enabling efficient data reuse and stability in learning.
# - They store experience tuples encountered by the agent, allowing for the random sampling of minibatches, which breaks correlations in the observation sequence.
# - In this section, we'll implement a simple yet functional Replay Buffer using Python's collections and PyTorch.

# %% [markdown] lang="en" tags=["slide"]
# ## Defining the Replay Buffer Class
# - The Replay Buffer class is initiated to store transitions with a specified maximum length.
# - It supports adding individual transitions to the buffer and sampling a random minibatch of transitions for training.
# - We'll explore the class structure and its critical methods: initialization, put, sample, and size.

# %%
import collections
import random
import torch

buffer_limit = 50000  # Define the maximum size of the buffer

class ReplayBuffer():
    # Initialize the buffer with a fixed maximum length
    def __init__(self):
        self.buffer = collections.deque(maxlen=buffer_limit)
    
    # Method to add a transition to the buffer
    def put(self, transition):
        self.buffer.append(transition)
    
    # Method to sample a minibatch of transitions
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

        # Transform lists into PyTorch tensors for the neural network training
        return torch.tensor(s_lst, dtype=torch.float), torch.tensor(a_lst), \
               torch.tensor(r_lst), torch.tensor(s_prime_lst, dtype=torch.float), \
               torch.tensor(done_mask_lst)
    
    # Method to get the current size of the buffer
    def size(self):
        return len(self.buffer)

# %% [markdown] lang="en" tags=["slide"]
# ## Functionality of the Replay Buffer
# - The `put` method allows for the transition data to be stored in the buffer until it reaches its limit.
# - The `sample` method randomly retrieves a subset of the buffer, which is used to train the DQN. It returns the components of the transitions as separate PyTorch tensors.
# - With these tensors, the DQN can learn from a diverse set of experiences, improving stability and efficiency in learning.
# - The `size` method returns the current number of transitions stored, useful for monitoring the buffer's status.
# %% [markdown] lang="en" tags=["slide"]
# ## Introduction to DQN
# - DQN stands for Deep Q-Network
# - It's an algorithm that combines Q-Learning with deep neural networks
# - DQNs can handle high-dimensional, continuous spaces

# %% [markdown] lang="en" tags=["slide"]
# ## Defining a Q-Network
# - We define a neural network model to approximate the Q-function
# - The neural network takes the state as input and outputs the Q-value for each action
# - Let's start by defining our Q-Network using PyTorch

# %%
import torch
import torch.nn as nn
import torch.nn.functional as F
import random

class Qnet(nn.Module):
    def __init__(self):
        super(Qnet, self).__init__()
        self.fc1 = nn.Linear(4, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, 2)

# %% [markdown] lang="en" tags=["slide"]
# ## Network Forward Pass
# - The forward method propagates the input through the network
# - Activation functions like ReLU are used for non-linearity
# - The output layer does not use an activation function as we are predicting Q-values

# %%
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# %% [markdown] lang="en" tags=["slide"]
# ## Action Selection
# - DQNs select actions based on the epsilon-greedy policy
# - With a probability of epsilon, we select a random action
# - Otherwise, we choose the action with the highest Q-value

# %%
    def sample_action(self, obs, epsilon):
        out = self.forward(obs)
        coin = random.random()
        if coin < epsilon:
            return random.randint(0,1)
        else: 
            return out.argmax().item()

# %% [markdown] lang="en" tags=["slide"]
# ## Recap and Next Steps
# - We've defined our Qnet class with methods for forward pass and action selection
# - Qnet will serve as the backbone for our DQN agent
# - Next, we will explore how to train this network and implement the DQN algorithm
# %% [markdown] lang="en" tags=["slide"]
# ## Training a DQN - Overview
# - Discuss the purpose and components of the `train()` function
# - Explain the critical steps in the Deep Q-Network (DQN) training loop
# - Introduce the parameters and tools used in training a DQN

# %% [markdown] lang="en" tags=["slide"]
# ## Memory Sampling
# - Memory sampling is crucial for breaking correlation between consecutive samples
# - A random batch of experiences is drawn from the memory buffer
# - This technique is also known as Experience Replay

# %%
def train(q, q_target, memory, optimizer):
    for i in range(10):
        s,a,r,s_prime,done_mask = memory.sample(batch_size)

# %% [markdown] lang="en" tags=["slide"]
# ## Calculating Q-values
# - Calculating current and future Q-values using the DQN and target DQN
# - Utilizing `gather` to select the Q-value for the action taken
# - Computing the maximum Q-value for the next state

# %%
        q_out = q(s)
        q_a = q_out.gather(1,a)
        max_q_prime = q_target(s_prime).max(1)[0].unsqueeze(1)

# %% [markdown] lang="en" tags=["slide"]
# ## Computing the Loss
# - Formulating the loss as the difference between the Q-values and the target values
# - Target values are computed considering the reward and discounted future Q-values
# - Usage of Smooth L1 Loss for stable training

# %%
        target = r + gamma * max_q_prime * done_mask
        loss = F.smooth_l1_loss(q_a, target)

# %% [markdown] lang="en" tags=["slide"]
# ## Optimizing the Network
# - Zeroing gradients to prevent accumulation
# - Performing backpropagation to compute gradients
# - Updating network weights with a step of the optimizer

# %%
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
# %% [markdown] lang="en" tags=["slide"]
# ## Introduction to DQN (Deep Q-Network)
# - The DQN algorithm combines Q-learning with deep neural networks to let the agent learn optimal policies.
# - Here, we implement a DQN to play CartPole, a balancing pole game.
# - We'll start with setting up the environment and initializing our network.

# %% [markdown] lang="en" tags=["slide"]
# ## Setting Up the CartPole Environment
# - We use Gym, a toolkit for developing and comparing reinforcement learning algorithms.
# - The initial setup involves creating the environment and initializing the Q-Networks.
# - ReplayBuffer is used for the experience replay mechanism critical for stabilizing training.

# %%
import gym
import torch
import torch.optim as optim

from qnet import Qnet # Assuming qnet module is provided and includes the Qnet class and ReplayBuffer class
from train import train # Assuming train module is provided and includes the training loop procedure

def main():
    env = gym.make('CartPole-v1')
    q = Qnet()
    q_target = Qnet()
    q_target.load_state_dict(q.state_dict())
    memory = ReplayBuffer()

# %% [markdown] lang="en" tags=["slide"]
# ## Optimization Setup
# - The Adam optimizer is used for adjusting network weights.
# - Epsilon is the exploration rate, which we'll linearly anneal from 8% to 1%.
# - The main loop performs interactions with the environment and updates the Q-network.

# %%
    learning_rate = 0.0004
    optimizer = optim.Adam(q.parameters(), lr=learning_rate)
    print_interval = 20
    score = 0.0  

# %% [markdown] lang="en" tags=["slide"]
# ## Main Training Loop
# - The loop iterates over episodes, selecting actions and updating the Q-network.
# - After every episode, it checks if the memory buffer is large enough to train the network.
# - The target network is updated at fixed intervals to stabilize learning.

# %%
    for n_epi in range(10000):
        epsilon = max(0.01, 0.08 - 0.01*(n_epi/200)) # Linear annealing from 8% to 1%
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
# ## Conclusion and Cleanup
# - By the end of training, the DQN agent should have learned to balance the pole on the cart.
# - It's important to always close the environment after training to free up resources.
# - Improvements can include adjusting hyperparameters, or trying different reward structures and architectures.

# %%
if __name__ == '__main__':
    main()
# %% [markdown] lang="en" tags=["slide"]
# ## Introduction to DQN
# - Deep Q-Networks (DQN) blend Q-Learning with deep neural networks to allow agents to learn directly from high-dimensional sensory inputs.
# - This approach was famously applied by DeepMind to learn playing Atari games from pixel inputs.
# - In this notebook, we will build a basic DQN model for a simple environment.

# %% [markdown] lang="en" tags=["slide"]
# ## Setting up the Environment
# - We will use OpenAI Gym's CartPole environment as a testbed.
# - The goal is to balance a pole on a cart by moving the cart left or right.
# - It is a simple but effective environment for demonstrating the capabilities of a DQN agent.

# %%
import gym
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# Create the environment
env = gym.make('CartPole-v1')


# %% [markdown] lang="en" tags=["slide"]
# ## Defining the Neural Network for DQN
# - The neural network will serve as the function approximator for our Q-values.
# - It takes the environment's state as input and outputs the Q-value for each action.
# - We use PyTorch to define our network.

# %%
class DQN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(DQN, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(input_size, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, output_size)
        )
    
    def forward(self, x):
        return self.network(x)


# %% [markdown] lang="en" tags=["slide"]
# ## Setting up the Training Loop
# - Training involves iteratively playing the game, storing experiences, and updating the model based on those experiences.
# - We sample actions using an epsilon-greedy strategy to balance exploration and exploitation.
# - Let's set up the main components needed for training our DQN agent.

# %%
def epsilon_greedy(state, epsilon):
    # Implement epsilon greedy action selection
    if np.random.rand() < epsilon:
        return env.action_space.sample()  # Explore
    else:
        with torch.no_grad():
            return model(state).argmax().item()  # Exploit

# %% [markdown] lang="en" tags=["slide"]
# ## Training the DQN Agent
# - We will now define the training loop for our DQN agent.
# - This loop involves running episodes, selecting actions, storing transitions, and updating the model.

# %%
# Hyperparameters
epochs = 1000
batch_size = 32
gamma = 0.99
epsilon_start = 1.0
epsilon_end = 0.01
epsilon_decay = 0.995
learning_rate = 0.0001

# Model, optimizer, and loss function
model = DQN(env.observation_space.shape[0], 64, env.action_space.n)
optimizer = optim.Adam(model.parameters(), lr=learning_rate)
loss_fn = nn.MSELoss()

# Training loop
for epoch in range(epochs):
    state = env.reset()
    state = torch.FloatTensor(state).unsqueeze(0)
    total_reward = 0
    done = False
    
    while not done:
        epsilon = max(epsilon_end, epsilon_start * (epsilon_decay ** epoch))
        action = epsilon_greedy(state, epsilon)
        
        next_state, reward, done, _ = env.step(action)
        next_state = torch.FloatTensor(next_state).unsqueeze(0)
        
        with torch.no_grad():
            next_q_values = model(next_state)
            max_next_q_value = next_q_values.max(1)[0]
            target_q_value = reward + (1 - done) * gamma * max_next_q_value
        
        pred_q_value = model(state)[0][action]
        
        loss = loss_fn(pred_q_value, target_q_value)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        state = next_state
        total_reward += reward
        
    if epoch % 100 == 0:
        print(f"Epoch: {epoch}, Total Reward: {total_reward}")
        

# %% [markdown] lang="en" tags=["slide"]
# ## Evaluating the DQN Agent
# - After training, it's important to evaluate our agent's performance in the environment without exploration noise.
# - This will give us a clearer picture of how well our agent has learned to solve the task.

# %%
total_rewards = []
for _ in range(100):
    state = env.reset()
    state = torch.FloatTensor(state).unsqueeze(0)
    total_reward = 0
    done = False
    
    while not done:
        action = model(state).argmax().item()  # Choose best action
        state, reward, done, _ = env.step(action)
        state = torch.FloatTensor(state).unsqueeze(0)
        total_reward += reward
    total_rewards.append(total_reward)

print(f"Average Reward: {np.mean(total_rewards)}")
# j2 from 'macros.j2' import header
# {{ header("DQN", "DQN") }}

# j2 from 'macros.j2' import header
# {{ header("DQN", "DQN") }}

# j2 from 'macros.j2' import header
# {{ header("test", "test") }}

