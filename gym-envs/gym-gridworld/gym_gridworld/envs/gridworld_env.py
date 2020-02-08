import gym
from gym import error, spaces, utils
from gym.utils import seeding


class GridworldEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    action_space = ['up', 'down', 'left', 'right']
    observation_space = None

    def __init__(self):
        self.size = 3
        self.reward = 1

        self.objPosX = 0
        self.objPosY = 0
        self.playerPosX = 2
        self.playerPosY = 2

        self._gen_world()

    def step(self, action):
        self._move(action)
        self._gen_world()

        obs = self.world
        reward, done = self._get_reward()

        return obs, reward, done, {}

    def reset(self):
        self.objPosX = 0
        self.objPosY = 0
        self.playerPosX = 2
        self.playerPosY = 2

        self._gen_world()
        obs = self.world

        return obs

    def render(self, mode='human'):
        for i in self.world:
            print('|%s|' % ', '.join(map(str, i)))

    def _gen_world(self):
        self.world = [[0 for i in range(self.size)] for j in range(self.size)]
        self.world[self.objPosY][self.objPosX] = self.reward
        self.world[self.playerPosY][self.playerPosX] = 8

    def _move(self, action):
        if action == 'up' and self.playerPosY > 0:
            self.playerPosY -= 1
        elif action == 'down' and self.playerPosY < self.size - 1:
            self.playerPosY += 1
        elif action == 'left' and self.playerPosX > 0:
            self.playerPosX -= 1
        elif action == 'right' and self.playerPosX < self.size - 1:
            self.playerPosX += 1
        else:
            pass

    def _get_reward(self):
        if self.playerPosX == self.objPosX and self.playerPosY == self.objPosY:
            return 0, True
        else:
            return -1, False
