import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

class GridworldV2Env(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, size):
        self.action_space = spaces.Discrete(4)
        self.observation_space = np.identity(size*size).tolist()

        self.terminal_state = self.observation_space[-1]
        self.world = self.observation_space[0]

        self.size = size

        sqr_size = size * size

        tr = {}

        iterator = np.arange(sqr_size).reshape(size, size)
        iterator = np.nditer(iterator, flags=['multi_index'])
        while not iterator.finished:
            index = iterator.iterindex
            row, col = iterator.multi_index

            tr[index] = {a: [self.observation_space[index], -1] for a in range(4)}

            if row > 0:
                tr[index][UP][0] = self.observation_space[index - size]
            if row < size - 1:
                tr[index][DOWN][0] = self.observation_space[index + size]
            if col > 0:
                tr[index][LEFT][0] = self.observation_space[index - 1]
            if col < size - 1:
                tr[index][RIGHT][0] = self.observation_space[index + 1]

            if tr[index][UP][0] == self.terminal_state:
                tr[index][UP][1] = 0
            if tr[index][DOWN][0] == self.terminal_state:
                tr[index][DOWN][1] = 0
            if tr[index][LEFT][0] == self.terminal_state:
                tr[index][LEFT][1] = 0
            if tr[index][RIGHT][0] == self.terminal_state:
                tr[index][RIGHT][1] = 0

            iterator.iternext()

        self.tr = tr

    def step(self, action):
        world_index = self.observation_space.index(self.world)
        self.world = self.tr[world_index][action][0]
        obs = self.world
        if obs == self.terminal_state:
            reward = 0
            done = True
        else:
            reward = -1
            done = False

        return obs, reward, done, {}

    def reset(self):
        self.world = self.observation_space[0]
        obs = self.world
        return obs

    def render(self, mode='human'):
        print(np.reshape(self.world, (self.size, self.size)))
