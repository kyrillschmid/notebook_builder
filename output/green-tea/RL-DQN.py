# j2 from 'macros.j2' import header
# {{ header("DQN with PyTorch", "DQN with PyTorch") }}

# j2 from 'macros.j2' import header
# {{ header("DQN with PyTorch", "DQN with PyTorch") }}

# %% [markdown] lang="en" tags=["slide"]
# ## Importing Required Libraries
# - We start with importing some basic libraries like:
#   - gym: the OpenAI gym for the reinforcement learning environment
#   - collections: to use high performance container datatypes
#   - random: for generating random numbers
# - Then, we import functionality from PyTorch library including:
#   - the `nn` module for building neural networks
#   - the `functional` module for operations like activation functions
#   - the `optim` module for various optimization algorithms

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
# - Here, we set the learning rate, gamma (discount factor), buffer limit and batch size as per our requirements.

# %%
#Hyperparameters
learning_rate = 0.0005
gamma         = 0.98
buffer_limit  = 50000
batch_size    = 32

# %% [markdown] lang="en" tags=["slide"]
# ## Creating a Replay Buffer Class
# - The Replay Buffer class is defined to store and manage the agent's experiences.
# - It comprises methods such as 'put' for adding transitions to the buffer and 'sample' for randomly selecting a batch of transitions.

# %%
class ReplayBuffer():
    def __init__(self):
        self.buffer = collections.deque(maxlen=buffer_limit)
    
    def put(self, transition):
        self.buffer.append(transition)
    
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
    
    def size(self):
        return len(self.buffer)

# %% [markdown] lang="en" tags=["slide"]
# ## Creating the Q-network Class
# - The Q-Network class is the Deep Q-Network, built using PyTorch's nn.Module base class.
# - It contains a forward method that defines the forward propagation of the network and a method to sample an action based on the observation and epsilon for the ε-greedy strategy.

# %%
class Qnet(nn.Module):
    def __init__(self):
        super(Qnet, self).__init__()
        self.fc1 = nn.Linear(4, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x
      
    def sample_action(self, obs, epsilon):
        out = self.forward(obs)
        coin = random.random()
        if coin < epsilon:
            return random.randint(0,1)
        else : 
            return out.argmax().item()

# %% [markdown] lang="en" tags=["slide"]
# ## Creating the Training Function
# - The `train` function uses the Q network, Q target network, Replay Buffer, and an Optimizer to train our model.
# - It includes computation of the Q values and  the Q target values, calculation of the loss, and then backpropagation of the loss through the network using gradient descent.

# %%
def train(q, q_target, memory, optimizer):
    for i in range(10):
        s,a,r,s_prime,done_mask = memory.sample(batch_size)

        q_out = q(s)
        q_a = q_out.gather(1,a)
        max_q_prime = q_target(s_prime).max(1)[0].unsqueeze(1)
        target = r + gamma * max_q_prime * done_mask
        loss = F.smooth_l1_loss(q_a, target)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

# %% [markdown] lang="en" tags=["slide"]
# ## Main Function
# - The `main` function is where the main logic of our reinforcement learning implementation resides.
# - It includes the creation of the environment (CartPole v1) and initializations of Q network, Q target, memory etc.
# - The function also contains the main learning loop, where the agent interacts with the environment and where the training function is called when we have enough experiences in the memory.

# %%
def main():
    env = gym.make('CartPole-v1')
    q = Qnet()
    q_target = Qnet()
    q_target.load_state_dict(q.state_dict())
    memory = ReplayBuffer()

    print_interval = 20
    score = 0.0  
    optimizer = optim.Adam(q.parameters(), lr=learning_rate)

    for n_epi in range(10000):
        epsilon = max(0.01, 0.08 - 0.01*(n_epi/200)) #Linear annealing from 8% to 1%
        s, _ = env.reset()
        done = False

        while not done:
            a = q.sample_action(torch.from_numpy(s).float(), epsilon)      
            s_prime, r, done, truncated, info = env.step(a)
            done_mask = 0.0 if done else 1.0
            memory.put((s, a, r/100.0, s_prime, done_mask))
            s = s_prime

            score += r
            if done:
                break
            
        if memory.size() > 2000:
            train(q, q_target, memory, optimizer)

        if n_epi%print_interval==0 and n_epi!=0:
            q_target.load_state_dict(q.state_dict())
            print("n_episode :{}, score : {:.1f}, n_buffer : {}, eps : {:.1f}%".format(
                                                            n_epi, score/print_interval, memory.size(), epsilon*100))
            score = 0.0
    env.close()

# %% [markdown] lang="en" tags=["slide"]
# ## Calling the Main function
# - Finally, we will call our `main` function which encapsulates our entire program logic.
# - If the code is executed as a standalone script, `__name__` will be `__main__` and the `main` function will be executed.

# %%
if __name__ == '__main__':
    main()
