from gym.envs.registration import register

register(
    id='gridworld-v0',
    entry_point='gym_gridworld.envs:GridworldEnv',
)

register(
    id='gridworld-v2',
    entry_point='gym_gridworld.envs:GridworldV2Env',
)

register(
    id='gridworld-v3',
    entry_point='gym_gridworld.envs:GridworldV3Env',
)

register(
    id='gridworld-v4',
    entry_point='gym_gridworld.envs:GridworldMontecarloEnv',
)