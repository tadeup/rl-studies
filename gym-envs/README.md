conda activate rl37

pip install -e gym-gridworld

pip install -e .

gym.make('gym_gridworld:gridworld-v0') 