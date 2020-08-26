from gym_derk.envs import DerkEnv
import logging
logging.basicConfig(level = logging.INFO)

env = DerkEnv(
  mode='battle'
)

while True:
  observation_n = env.reset()
  while True:
    # env.render()
    action_n = [env.action_space.sample() for i in range(env.n_agents)]
    observation_n, reward_n, done_n, info = env.step(action_n)
    if all(done_n):
      print("Episode finished")
      break
env.close()