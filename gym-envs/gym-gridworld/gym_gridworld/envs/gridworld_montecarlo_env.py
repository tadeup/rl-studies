import gym
from gym import error, spaces, utils
from gym.utils import seeding

import numpy as np

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3


class GridworldMontecarloEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self, size):
        self.size = size
        self.action_space = spaces.Discrete(4)
        self.observation_space = np.identity(size * size).tolist()
        self.world = np.zeros(size * size).reshape(size, size)
        self.playerPos = [0,0]
        self.goalPos = [size-1, size-1]

    def step(self, action):
        if action == UP and self.playerPos[0] > 0:
            self.playerPos[0] -= 1

        if action == RIGHT and self.playerPos[1] < self.size - 1:
            self.playerPos[1] += 1

        if action == DOWN and self.playerPos[0] < self.size - 1:
            self.playerPos[0] += 1

        if action == LEFT and self.playerPos[1] > 0:
            self.playerPos[1] -= 1

        obs = self._get_obs()
        obs = obs.flatten().tolist()

        if self.playerPos == self.goalPos:
            reward = 0
            done = True
        else:
            reward = -1
            done = False

        return obs, reward, done, {}

    def reset(self):
        self.playerPos = [0,0]
        obs = self._get_obs()
        obs = obs.flatten().tolist()
        return obs

    def render(self, mode='human'):
        obs = self._get_obs()
        print(obs)

    def _get_obs(self):
        obs = self.world.copy()
        obs[tuple(self.playerPos)] = 1
        return obs
