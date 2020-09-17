from gym_derk.envs import DerkEnv, EpisodeResetError
from argparse import ArgumentParser
import logging
logging.basicConfig(level = logging.INFO)

parser = ArgumentParser()
parser.add_argument("-s", "--serve", action="store_true", dest="serve", default=False)
args = parser.parse_args()

env = DerkEnv(
  server_port=8789 if args.serve else None
)

while True:
  try:
    observation_n = env.reset()
    while True:
      # env.render()
      action_n = [env.action_space.sample() for i in range(env.n_agents)]
      observation_n, reward_n, done_n, info = env.step(action_n)
      if all(done_n):
        print("Episode finished")
        break
  except EpisodeResetError:
    print('Episode reset')
env.close()
